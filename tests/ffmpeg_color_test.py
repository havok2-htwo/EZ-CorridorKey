"""Regression tests for FFmpeg colour filter construction."""

import backend.ffmpeg_tools as ffmpeg_tools


def test_yuv_input_with_gbr_matrix_uses_fallback_matrix(caplog):
    vf = ffmpeg_tools.build_exr_vf({
        "pix_fmt": "yuv422p10le",
        "width": 1920,
        "height": 1080,
        "color_space": "gbr",
        "color_primaries": "bt709",
        "color_transfer": "bt709",
        "color_range": "tv",
        "bits_per_raw_sample": 10,
    })

    assert vf == "scale=in_color_matrix=bt709:in_range=tv,format=gbrpf32le"
    assert "reported matrix=gbr" in caplog.text
