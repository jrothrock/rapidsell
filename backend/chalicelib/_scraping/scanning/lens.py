"""
Utilizes serpapi to gather results from Google lens.

Eventually, it may be best to do this ourselves using
playwright, a captcha bypasser, and a chromium lambda layer.
Unfortunuately, there are no python chromium layers currently
(that I have been able to find so far), so this may need to be
built.
"""
import os
import typing

import requests

from chalicelib._dynamo.scanning import ScannedImageModel

FORMATTABLE_RAPID_SELL_ENDPOINT = "https://api.rapidsell.io/scanning/img/{img}"

FORMATTABLE_SERP_API_ENDPOINT = (
    "https://serpapi.com/search?engine=google_lens&url={url}&api_key={api_key}"
)


def _capture_important_data(
    json_response: dict[str, typing.Any]
) -> dict[str, typing.Any]:
    print(json_response)

    # If there's text in the image, this will find it.
    if json_response.get("text_results"):
        text_results = json_response["text_results"]
        title_key_words = [x["text"] for x in text_results]
        title = " ".join(title_key_words)
    else:
        # A better way to do this, is to loop over the visual
        # results and perform TF-IDF on them to extract the most likely
        # title.
        title = json_response["visual_matches"][0]["title"]

    return {"title": title}


def run(uuid_for_image: str, image_s3_key: str, image_s3_bucket: str):
    """Get the response from Google lens on what this image could be."""
    image_url = FORMATTABLE_RAPID_SELL_ENDPOINT.format(img=uuid_for_image)
    serp_api_key = os.environ.get("SERP_API_KEY", "")
    serp_api_endpoint = FORMATTABLE_SERP_API_ENDPOINT.format(
        url=image_url, api_key=serp_api_key
    )

    response = requests.get(serp_api_endpoint)
    json_response: dict[str, typing.Any] = response.json()

    # Bail if we don't succeed.
    if json_response["search_metadata"]["status"] != "Success":
        return

    important_data = _capture_important_data(json_response)

    user_name = image_s3_key.split("/")[0]

    pk = f"ScannedImage#{user_name}#{uuid_for_image}"
    sk = "ScannedImage#meta"
    scanned_image = ScannedImageModel(
        pk,
        sk,
        image_key=image_s3_key,
        image_bucket=image_s3_bucket,
        serp_found_title=important_data["title"],
    )
    scanned_image.save()
