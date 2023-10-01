"""
Utilizes serpapi to gather results from Google lens.

Eventually, it may be best to do this ourselves using
playwright, a captcha bypasser, and a chromium lambda layer.
Unfortunuately, there are no python chromium layers currently
(that I have been able to find so far), so this may need to be
built.
"""
import difflib
import os
import statistics
import typing

import requests

from chalicelib._dynamo.scanning import ScannedImageModel

FORMATTABLE_RAPID_SELL_ENDPOINT = "https://api.rapidsell.io/scanning/img/{img}"

FORMATTABLE_SERP_API_ENDPOINT = (
    "https://serpapi.com/search?engine=google_lens&url={url}&api_key={api_key}"
)


def _capture_important_information(
    json_response: dict[str, typing.Any]
) -> dict[str, typing.Any]:
    """Capture the important information from the serp api response."""
    titles = [item["title"] for item in json_response["visual_matches"]]
    # Google is propbably predicting the best title.
    title = titles[0]

    # Somewhat arbitrary
    sequence_matcher_threshold = 0.85
    prices = []
    for item in json_response["visual_matches"]:
        if item.get("price"):

            similarity = difflib.SequenceMatcher(None, title, item["title"]).ratio()

            if similarity > sequence_matcher_threshold:
                prices.append(item["price"]["extracted_value"])

    if len(prices) > 0:
        average_price = statistics.mean(prices)
    else:
        average_price = None

    return {"title": title, "price": average_price}


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

    important_information = _capture_important_information(json_response)
    title = important_information["title"]
    price = important_information["price"]

    user_name = image_s3_key.split("/")[0]

    pk = f"ScannedImage#{user_name}#{uuid_for_image}"
    sk = "ScannedImage#meta"
    scanned_image = ScannedImageModel(
        pk,
        sk,
        image_key=image_s3_key,
        image_bucket=image_s3_bucket,
        serp_found_title=title,
        serp_found_price=price,
        serp_json_response=str(json_response),
    )
    scanned_image.save()
