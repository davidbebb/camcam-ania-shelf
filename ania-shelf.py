# Shelf to replace annoying towel holder.

width = 320
height = 150
origin = V(0, 0)
thickness = 12.5

toothbrush_holder_dia = 80
tray_diameter = 90
x_spacing = 60
y_offset = -10
toothbrush_holder_centre = origin-V(toothbrush_holder_dia/2, 0)-V(x_spacing/2, 0)+V(0, y_offset)
tray_centre=origin+V(tray_diameter/2, 0)+V(x_spacing/2, 0)+V(0, y_offset)


mount_spacing = 150
plane = camcam.add_plane(Plane('xy', cutter='1/8_endmill'))

plane.add_layer('layer_name', 'plywood', thickness)
# ('layer_name', 'material', thickness,
# back (extra layer to mill on both sides)True/False),
# isback (mirrors when cut left-right) True/False,'colour')


border = Path(closed=True, side='out')

border.add_point(PIncurve  (origin+V(width/2, height/2),
                            radius=0,
                            direction='cw'))

border.add_point(PIncurve  (origin+V(width/2, -height/2),
                            radius=10,
                            direction='cw'))

border.add_point(PIncurve  (origin+V(-width/2, -height/2),
                            radius=10,
                            direction='cw'))

border.add_point(PIncurve(  origin+V(-width/2, height/2),
                            radius=0,
                            direction='cw'))

shelf_part = Part(  name='shelf',
                    layer='layer_name',
                    ignore_border=False,
                    border=border)

shelf = plane.add(shelf_part)

shelf.add(Hole(toothbrush_holder_centre, toothbrush_holder_dia/2))
shelf.add(Hole(tray_centre, tray_diameter/2))
