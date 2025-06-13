import reflex as rx
 

def backgroundSetter():
    return rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            z_index="-1",  # Behind content
            background_size="60px 60px",
            background_image="linear-gradient(hsl(0, 0%, 35%) 1px, transparent 1px), linear-gradient(to right, transparent 99%, hsl(0, 0%, 40%) 100%)",
            mask="radial-gradient(45% 50% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0))",
            mask_repeat="no-repeat",
            mask_size="100% 100%",
    ),

#this can be called w/ background.backgroundSetter