Use camera name `chest_rgbd`. Capture returns a snapshot ID that persists between
cells. Use the same camera and ID for RGB and segmentation. Use `display(rgb)`
to see the original image in the next model turn. Read its native array shape
as (height, width, channels). Pick an interior pixel in (row, column) order.
Inspect `display(result.overlay_rgb)` when an overlay is available. A localized
point describes a visible surface in the URDF world frame in metres. The human
reviewer can compare the source image and overlay after the episode.
