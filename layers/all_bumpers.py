from static_obj.bumper import Bumper


def add_center_bumper(all_sprites, bumpers):
    Bumper(
        center_circle=[250, 330],
        img='images/bumper_center_250_330.png',
        all_sprites=all_sprites,
        bumpers=bumpers,
        name='bumper_center_250_330'
    )


def add_lateral_bumper(all_sprites, bumpers):
    Bumper(
        center_circle=[-270, 307],
        img='images/bumper_left_-270_307.png',
        all_sprites=all_sprites,
        bumpers=bumpers,
        name='bumper_left_-270_307'
    )

    Bumper(
        center_circle=[770, 307],
        img='images/bumper_right_770_307.png',
        all_sprites=all_sprites,
        bumpers=bumpers,
        name='bumper_right_770_307'
    )
