image astralis_wide = "images/bg/astralis_wide.png"

## Character Creation

image magic_circle: 
    "images/ui/ui_magiccircle.png"
    zoom 0.21

image stat_logo:
    "images/ui/ui_statlogo.png"
    zoom 0.21

image stat_argent:
    "images/ui/ui_stat_argent.png"
    zoom 0.21

image stat_cobalt:
    "images/ui/ui_stat_cobalt.png"
    zoom 0.21

image stat_viridian:
    "images/ui/ui_stat_viridian.png"
    zoom 0.21

image stat_rose:
    "images/ui/ui_stat_rose.png"
    zoom 0.21

image stat_violet:
    "images/ui/ui_stat_violet.png"
    zoom 0.21

image stat_scarlet:
    "images/ui/ui_stat_scarlet.png"
    zoom 0.21

image stat_aurum:
    "images/ui/ui_stat_aurum.png"
    zoom 0.21

image stat_obsidian:
    "images/ui/ui_stat_obsidian.png"
    zoom 0.21

# Invisible Radar Chart Tooltip
image stat_argent_tooltip:
    "images/ui/ui_argent_tooltip.png"
    zoom 0.21
    alpha 0.003
image stat_aurum_tooltip:
    "images/ui/ui_aurum_tooltip.png"
    zoom 0.21
    alpha 0.003
image stat_cobalt_tooltip:
    "images/ui/ui_cobalt_tooltip.png"
    zoom 0.21
    alpha 0.003
image stat_obsidian_tooltip:
    "images/ui/ui_obsidian_tooltip.png"
    zoom 0.21
    alpha 0.003
image stat_viridian_tooltip:
    "images/ui/ui_viridian_tooltip.png"
    zoom 0.21
    alpha 0.003
image stat_violet_tooltip:
    "images/ui/ui_violet_tooltip.png"
    zoom 0.21
    alpha 0.003
image stat_rose_tooltip:
    "images/ui/ui_rose_tooltip.png"
    zoom 0.21
    alpha 0.003
image stat_scarlet_tooltip:
    "images/ui/ui_scarlet_tooltip.png"
    zoom 0.21
    alpha 0.003

#

image astralis_logo = "images/ui/astralis_logo.png"
image argent_logo = "images/ui/ui_argentlinecolor.png"
image aurum_logo = "images/ui/ui_aurumlinecolor.png"
image cobalt_logo = "images/ui/ui_cobaltlinecolor.png"
image obsidian_logo = "images/ui/ui_obsidianlinecolor.png"
image rose_logo = "images/ui/ui_roselinecolor.png"
image scarlet_logo = "images/ui/ui_scarletlinecolor.png"
image violet_logo = "images/ui/ui_violetlinecolor.png"
image viridian_logo = "images/ui/ui_viridianlinecolor.png"

###
### ANIMATIONS
###

# RADAR CHART

transform spinner_base:
    zoom 0.0
    align (0.5, 0.5)
    rotate 0.0
    alpha 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        linear 1.0 zoom 1.0
    parallel:
        pause 0
        linear 1.0 alpha 1.0

transform spinner_data:
    zoom 0.0
    align (0.5, 0.5)
    rotate 0.0
    alpha 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        pause 1.35
        linear 1.0 zoom 1.0
    parallel:
        linear 1.35 alpha 1.0

transform spinner_labels1:
    align (0.5, 0.5)
    alpha 0.0
    zoom 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        linear 1.0 zoom 1.0
    parallel:
        pause 1.05
        linear 0.5 alpha 1.0  
transform spinner_labels2:
    align (0.5, 0.5)
    alpha 0.0
    zoom 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        linear 1.0 zoom 1.0
    parallel:
        pause 1.1
        linear 0.5 alpha 1.0
transform spinner_labels3:
    align (0.5, 0.5)
    alpha 0.0
    zoom 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        linear 1.0 zoom 1.0
    parallel:
        pause 1.15
        linear 0.5 alpha 1.0
transform spinner_labels4:
    align (0.5, 0.5)
    alpha 0.0
    zoom 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        linear 1.0 zoom 1.0
    parallel:
        pause 1.2
        linear 0.5 alpha 1.0
transform spinner_labels5:
    align (0.5, 0.5)
    alpha 0.0
    zoom 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        linear 1.0 zoom 1.0
    parallel:
        pause 1.25
        linear 0.5 alpha 1.0
transform spinner_labels6:
    align (0.5, 0.5)
    alpha 0.0
    zoom 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        linear 1.0 zoom 1.0
    parallel:
        pause 1.3
        linear 0.5 alpha 1.0
transform spinner_labels7:
    align (0.5, 0.5)
    alpha 0.0
    zoom 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        linear 1.0 zoom 1.0
    parallel:
        pause 1.35
        linear 0.5 alpha 1.0
transform spinner_labels8:
    align (0.5, 0.5)
    alpha 0.0
    zoom 0.0
    parallel:
        linear 1.0 rotate 360
    parallel:
        linear 1.0 zoom 1.0
    parallel:
        pause 1.4
        linear 0.5 alpha 1.0