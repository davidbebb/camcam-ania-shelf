# Shelf to replace annoying towel holder.

width = 250
height = 150
origin = V(0, 0)
thickness = 12.5

toothbrush_holder_dia = 80
tray_diameter = 90
x_spacing = 30
x_offset = -15
y_offset = -10
x_offset_shelf = 45
tab_depth = 9
toothbrush_holder_centre = origin-V(toothbrush_holder_dia/2, 0)-V(x_spacing/2, 0)+V(x_offset, y_offset)
tray_centre=origin+V(tray_diameter/2, 0)+V(x_spacing/2, 0)+V(x_offset, y_offset)

mount_spacing = 122

mount_screw_head_dia = 8

plane = camcam.add_plane(Plane('xy', cutter='1/8_endmill',isback=True))

plane.add_layer('layer_name', 'plywood', thickness)

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

leftX = ((-thickness/2)+mount_spacing/2)+x_offset_shelf

mountHolesLeft=shelf.add_path(
    FingerJointMid(
    	start = V(leftX,height/2),
    	end = V(leftX,(-height/2)+10),
    	side = 'left',
    	linemode = 'internal',
    	startmode = 'off',
    	endmode = 'off',
    	tab_length = 12,
    	thickness = thickness,
    	cutterrad = 0,#3.17/2,#cutterrad,
    	prevmode = 'off',
    	nextmode = 'off',
        fudge = -2,
        z1 = -tab_depth
    ),
    ['layer_name'],
)

rightX = ((-thickness/2)-mount_spacing/2)+x_offset_shelf

mountHolesRight=shelf.add_path(
    FingerJointMid(
    	start = V(rightX,height/2),
    	end = V(rightX,(-height/2)+10),
    	side = 'left',
    	linemode = 'internal',
    	startmode = 'off',
    	endmode = 'off',
    	tab_length = 12,
    	thickness = thickness,
    	cutterrad = 0,#3.17/2,#cutterrad,
    	prevmode = 'off',
    	nextmode = 'off',
        fudge = -2,
        z1 = -tab_depth
    ),
    ['layer_name'],
)
