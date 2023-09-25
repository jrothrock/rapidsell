"""Due to Google lens not working with presigned urls, we need to redirect."""
from chalice.app import Request
from chalice.app import Response

from chalicelib._dynamo.scanning import ScanningImageModel


def img_redirect_s3(request: Request, img_uuid: str):
    """Get the redirect image for google lens."""
    pk = f"ScanningImage#{img_uuid}"
    sk = "ScanningImage#meta"
    item = ScanningImageModel.get(pk, sk)

    return Response(body="", headers={"Location": item.signed_url}, status_code=301)
