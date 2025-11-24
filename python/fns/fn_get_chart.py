import os
from fastapi.responses import FileResponse
from fastapi.responses import Response

def fn_get_chart():
    chart_path = "chart.png"
    if not os.path.exists(chart_path):
        return {"error": "Chart not generated yet."}
    with open(chart_path, "rb") as f:
        img_bytes = f.read()
    return Response(
        content=img_bytes,
        media_type="image/png",
        headers={
            "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
            "Pragma": "no-cache",
            "Expires": "0",
        }
    )
    # return FileResponse(chart_path, media_type="image/png")