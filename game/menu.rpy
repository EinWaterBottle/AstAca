### GLOSSARY

init python:
    astralis_handbook = Encyclopaedia(name="Astralis Handbook")

    entry_scarlet = EncEntry(
        parent=astralis_handbook,
        name="Scarlet Magic",
        subject="Schools of Magic",

        image=Frame("images/ui/ui_scarletlinecolor.png"),

        text=enc_utils.text_block("""\
        Violent, passionate, and sincere. Few schools of magic are as 
        paradoxical as this one. Both handling the forces of life-giving 
        and fireball-spewing, long study and argument have categorized 
        the manipulation of raw, fervent energy as Scarlet Magic. 
        Its users often give this school a rather harsh reputation,
        as they tend to favor its more destructive and flashy side.

        Rivals to the Cobalt Falcons
        """)
    )

    entry_cobalt = EncEntry(
        parent=astralis_handbook,
        name="Cobalt Magic",
        subject="Schools of Magic",

        image=Frame("images/ui/ui_cobaltlinecolor.png"),

        text=enc_utils.text_block("""\
        Placeholder

        Rivals to the asdfasdfasdf
        """)
    )

    entry_obsidian = EncEntry(
        parent=astralis_handbook,
        name="Obsidian Magic",
        subject="Schools of Magic",

        image=Frame("images/ui/ui_obsidianlinecolor.png"),

        text=enc_utils.text_block("""\
        Placeholder

        Rivals to the asdfasdfds
        """)
    )

    entry_argent = EncEntry(
        parent=astralis_handbook,
        name="Argent Magic",
        subject="Schools of Magic",

        image=Frame("images/ui/ui_argentlinecolor.png"),

        text=enc_utils.text_block("""\
        Placeholder

        Rivals to the asdfasdfds
        """)
    )
    
    entry_viridian = EncEntry(
        parent=astralis_handbook,
        name="Viridian Magic",
        subject="Schools of Magic",

        image=Frame("images/ui/ui_viridianlinecolor.png"),

        text=enc_utils.text_block("""\
        Placeholder

        Rivals to the asdfasdfds
        """)
    )
        
    entry_rose = EncEntry(
        parent=astralis_handbook,
        name="Rose Magic",
        subject="Schools of Magic",

        image=Frame("images/ui/ui_roselinecolor.png"),

        text=enc_utils.text_block("""\
        Placeholder

        Rivals to the asdfasdfds
        """)
    )
    
    entry_violet = EncEntry(
        parent=astralis_handbook,
        name="Violet Magic",
        subject="Schools of Magic",

        image=Frame("images/ui/ui_violetlinecolor.png"),

        text=enc_utils.text_block("""\
        Placeholder

        Rivals to the asdfasdfds
        """)
    )
    
    entry_aurum = EncEntry(
        parent=astralis_handbook,
        name="Aurum Magic",
        subject="Schools of Magic",

        image=Frame("images/ui/ui_aurumlinecolor.png"),

        text=enc_utils.text_block("""\
        Placeholder

        Rivals to the asdfasdfds
        """)
    )
    


################################################################################
#  entry_button:
#    Component screen for a button that sets an Entry in an Encyclopaedia to
#    be the active one.
#
#    This screen is used by the vertical_list screen.
#
#    Args:
#        enc (Encyclopaedia): The encyclopaedia to use on this screen.
#        entry (EncEntry): The entry to associate with the button.
################################################################################

screen entry_button(enc, entry):
    button:
        style "encyclopaedia_list_button"

        action enc.SetEntry(entry)

        hbox:
            spacing 10
            text entry.name style "encyclopaedia_list_button_text"
            # If an entry is not locked and not viewed, display an indication
            # for the user.
            if (entry.locked is False) and (not entry.viewed):
                text _("New!") style "unread_entry_notice_text"


################################################################################
#  vertical_list:
#    Screen to display a vertical list of entry_button components.
#
#    The way buttons are displayed depends:
#    - On the Encyclopaedia's sorting mode,
#    - If buttons for locked entries should be shown
#    - If locked entries should be viewable with placeholder data.
#
#    This screen is used by the encyclopaedia_list screen.
#
#    Args:
#        enc (Encyclopaedia): The encyclopaedia to use on this screen.
################################################################################

screen vertical_list(enc):
    # The list used is chosen based on if we want to show locked entries on
    #   the entry select screen or not.
    if enc.sorting_mode == SortMode.SUBJECT:
        # Split entries by subject
        for key, group in groupby(enc.current_entries, attrgetter("subject")):
            text key style "encyclopaedia_list_subject_header" # The subject heading
            for entry in group:
                use entry_button(enc, entry)

    elif enc.sorting_mode == SortMode.NUMBER:
        for entry in enc.current_entries:
            hbox:
                spacing 10
                text "{:02}".format(entry.number) style "encyclopaedia_list_number_text"
                use entry_button(enc, entry)

    # If sorting Alphabetically, Reverse-Alphabetically, or by Unread.
    else:
        if enc.nest_alphabetical_sort:
            # Split entries by first letter
            for key, group in groupby(enc.current_entries, key=lambda x: x.name[0]):
                text key style "encyclopaedia_list_letter_text"  # The letter heading
                for entry in group:
                    use entry_button(enc, entry)

        else:
            for entry in enc.current_entries:
                use entry_button(enc, entry)


################################################################################
#    Encyclopaedia List:
#    Screen that's used to display the list of entries, the filter buttons, and the sorting buttons
#
#    Args:
#        enc (Encyclopaedia): The encyclopaedia to use on this screen.
################################################################################

screen encyclopaedia_list(enc):
    tag menu
    modal True

    # Active entries get shown automatically.
    # Ugly, but due to how ShowMenu() works, we need to put this on the screen,
    # not in an Action.
    # Generally, this is used by hyperlinks to jump directly to an EncEntry.
    on "show" action [
        If(enc.active, enc.SetEntry(enc.active)),
    ]

    # PLAYER NAME / MERITS / GOODWILL
    hbox:
        xalign 0.0
        yalign 0.0

        frame:

            add "images/characters/02_Default_Daniel_larger.png" zoom 0.25

        frame:
            xpadding 15
            ypadding 10

            vbox:
                spacing 15

                vbox:
                    spacing 20

                    text "{b}Name:{/b} [firstname] [lastname]"
                    text "{b}Pronouns:{/b} [They]/[Their]"
                    text "{b}House:{/b} [house]"
                    text "{b}Merits:{/b} [merits]"
                    text "{b}Goodwill:{/b} [goodwill]"

    # PLAYER STATS
    frame:
        xalign 0.0
        yalign 0.95
        xpadding 80
        ypadding 80

        hbox:
            spacing 40

            frame:
                background None
                xysize (300, 300)
                add "magic_circle" at spinner_base
                add "stat_argent" at spinner_labels1
                add "stat_cobalt" at spinner_labels2
                add "stat_viridian" at spinner_labels3
                add "stat_rose" at spinner_labels4
                add "stat_violet" at spinner_labels5
                add "stat_scarlet" at spinner_labels6
                add "stat_aurum" at spinner_labels7
                add "stat_obsidian" at spinner_labels8
                add stat_chart.chart_data at spinner_data
                #add stat_chart.chart_labels at spinner_labels

                # Invisible Imagebuttons for stat tooltips

                imagebutton:
                    focus_mask True
                    idle "stat_argent_tooltip"
                    action NullAction()
                    tooltip "[argent_text]: [argent]"
                    at spinner_labels1
                imagebutton:
                    focus_mask True
                    idle "stat_cobalt_tooltip"
                    action NullAction()
                    tooltip "[cobalt_text]: [cobalt]"
                    at spinner_labels2
                imagebutton:
                    focus_mask True
                    idle "stat_viridian_tooltip"
                    action NullAction()
                    tooltip "[viridian_text]: [viridian]"
                    at spinner_labels3
                imagebutton:
                    focus_mask True
                    idle "stat_rose_tooltip"
                    action NullAction()
                    tooltip "[rose_text]: [rose]"
                    at spinner_labels4
                imagebutton:
                    focus_mask True
                    idle "stat_violet_tooltip"
                    action NullAction()
                    tooltip "[violet_text]: [violet]"
                    at spinner_labels5
                imagebutton:
                    focus_mask True
                    idle "stat_scarlet_tooltip"
                    action NullAction()
                    tooltip "[scarlet_text]: [scarlet]"
                    at spinner_labels6
                imagebutton:
                    focus_mask True
                    idle "stat_aurum_tooltip"
                    action NullAction()
                    tooltip "[aurum_text]: [aurum]"
                    at spinner_labels7
                imagebutton:
                    focus_mask True
                    idle "stat_obsidian_tooltip"
                    action NullAction()
                    tooltip "[obsidian_text]: [obsidian]"
                    at spinner_labels8

    # GLOSSARY ON THE RIGHT
    frame:
        style_prefix "encyclopaedia"
        yfill True
        xsize 0.5
        xalign 1.0

        vbox:
            frame:
                style_prefix "encyclopaedia"
                xfill True

                text enc.name

            frame:
                style_prefix "encyclopaedia"
                xfill True

                hbox:
                    xfill True
                    # Percentage unlocked display
                    text _("[enc.percentage_unlocked] % Complete") style "encyclopaedia_header_text"

            frame:
                style_prefix "encyclopaedia"
                xfill True

                vbox:
                    spacing 6

                    hbox:
                        spacing 8

                        text _("Filter") style "encyclopaedia_header_text"

                        use dropdown(focus_name="diff_drop"):
                            text enc.filtering or _("---") style "encyclopaedia_subject_filters_button_text"

            vbox:
                hbox:
                    frame:
                        style_prefix "encyclopaedia"
                        ymaximum 1.0

                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True

                            ymaximum 0.908

                            vbox:
                                spacing 0
                                use vertical_list(enc) id "vertical list"

                frame:
                    style_prefix "encyclopaedia"

                    xfill True

                    hbox:
                        textbutton _("Return") action [enc.CloseActiveEntry(), Return()] style "encyclopaedia_close_button"

    use dropdown_options("diff_drop"):
        textbutton _("---"):
            action [enc.ClearFilter(), ClearFocus("diff_drop")]
            style "encyclopaedia_subject_filters_button"

        for subject in enc.subjects:
            textbutton subject:
                action [enc.FilterBySubject(subject), ClearFocus("diff_drop")]
                style "encyclopaedia_subject_filters_button"
    
    # TOOLTIP

    $ tooltip = GetTooltip()

    if tooltip:
        timer 0.02 repeat True action Function(get_mouse)
        $ mx = mouse_xy[0] - 30 # LR
        $ my = mouse_xy[1] + 30 # UD
        frame:
            pos(mx,my)
            vbox:
                spacing 5
                text tooltip:
                    size 25

################################################################################
#    Encyclopaedia Entry:
#    Screen that's used to display an individual EncEntry.
#
#    Args:
#        enc (Encyclopaedia): The encyclopaedia to use on this screen.
################################################################################

screen encyclopaedia_entry(enc):
    tag encyclopaedia_entry

    frame:
        style_prefix "encyclopaedia_entry"

        vbox:
            # Flavour text to indicate which entry we're currently on.
            frame:
                style_suffix "label_frame"

                text str(enc.active)

            # Buttons to swap between pages.
            frame:
                style_suffix "change_entry_frame"
                id "entry_nav"

                hbox:
                    style_suffix "change_entry_hbox"

                    # Previous / Next is relative to the sorting mode
                    textbutton _("Previous Entry") xalign .02 action enc.PreviousEntry() style_suffix "change_entry_button"
                    textbutton _("Next Entry") xalign .98 action enc.NextEntry() style_suffix "change_entry_button"

            # Entry text
            vbox:
                spacing 8
                # If the entry has an image
                if enc.active.current_page.has_image:
                    frame:
                        style_prefix "encyclopaedia_entry_image"

                        viewport:
                            scrollbars None
                            draggable True
                            mousewheel True
                            edgescroll (1.0, 1.0)

                            add enc.active.current_page.image

                frame:
                    style_prefix "encyclopaedia_entry_content"
                    id "entry_window"

                    if enc.active.current_page.has_image:
                        ymaximum 0.685
                    else:
                        ymaximum 0.846

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        vbox:
                            spacing 8
                            # Display the current entry's text
                            for item in enc.active.current_page.text:
                                text "[item]" style "encyclopaedia_entry_text"

            frame:
                style_prefix "encyclopaedia"
                xalign 1.0
                xfill True

                # If the entry has pages, add Prev/Next Page buttons
                if len(enc.active.pages) > 1:
                    hbox:
                        style "encyclopaedia_entry_change_entry_hbox"

                        textbutton _("Previous Page") xalign .02 action enc.PreviousPage() style "encyclopaedia_entry_change_entry_button"

                        # Flavour text to indicate which page out of the total is being viewed
                        $ total_pages = len(enc.active.pages)
                        text _("Page [enc.active.current_page.page_number] / [total_pages]") style "encyclopaedia_entry_page_label"

                        textbutton _("Next Page") xalign .98 action enc.NextPage() style "encyclopaedia_entry_change_entry_button"

                else:
                    xpadding 10
                    ypadding 10
                    text " " size 18 yalign 0.5

            frame:
                style_prefix "encyclopaedia"
                xfill True

                hbox:
                    xfill True
                    # Flavour text that displays the current sorting mode
                    textbutton _("Close Entry") id "close_entry_button" xalign .98 clicked enc.CloseActiveEntry() style "encyclopaedia_close_button"


###
# The select box for a dropdown.
###
screen dropdown(focus_name):
    frame:
        button:
            padding (0, 0, 0, 0)

            action CaptureFocus(focus_name)

            hbox:
                xfill True

                frame:
                    background None
                    xsize 0.9
                    transclude

                frame:
                    background None
                    xfill True
                    text "▼" style "dropdown_arrow"


###
# The options frame for a dropdown.
###
screen dropdown_options(focus_name):
    if GetFocusRect(focus_name):
        dismiss action ClearFocus(focus_name)

        nearrect:
            focus focus_name

            frame:
                modal True

                padding (6, 6, 6, 6)
                margin (-6, 6, 0, 0)

                has vbox

                transclude


######################
# Encyclopaedia Styles
######################
style dropdown_arrow is button_text:
    size 18
    xalign 1.0

style encyclopaedia_vbox is vbox:
    spacing 6

style encyclopaedia_frame is frame:
    padding (6, 6, 6, 6)

style encyclopaedia_header_text:
    yalign 0.5

    size 20

style encyclopaedia_sorting_label_text:
    xalign 0.5
    yalign 0.5
    size 14

style encyclopaedia_scrollbar is scrollbar

style encyclopaedia_vscrollbar is vscrollbar

style encyclopaedia_button is button

style encyclopaedia_button_text is button_text

style encyclopaedia_list_button is encyclopaedia_button:
    background Solid("#000")
    hover_background Solid(gui.hover_color)
    selected_background Solid(gui.accent_color)
    selected_hover_background Solid(gui.hover_color)
    xsize 1.0
    yalign 0.5
    padding (6, 0, 0, 0)

style encyclopaedia_list_button_text is encyclopaedia_button_text:
    size 18
    xalign 0.5
    color gui.accent_color
    hover_color "#000"
    selected_color "#000"
    insensitive_color "#3D3D3D"

style encyclopaedia_list_letter_text:
    size 24
    padding (10, 10, 10, 10)
    yalign 0.5

style encyclopaedia_list_number_text:
    size 18
    padding (10, 10, 10, 10)
    yalign 0.5

style unread_entry_notice_text:
    size 18
    padding (10, 10, 10, 10)
    yalign 0.5

style encyclopaedia_entry_text is default:
    size 16

style encyclopaedia_list_subject_header:
    size 24

style encyclopaedia_subject_filters_button is encyclopaedia_button:
    xfill False

style encyclopaedia_subject_filters_button_text is encyclopaedia_button_text:
    size 18

style encyclopaedia_sort_by
style encyclopaedia_sort_by_button is encyclopaedia_button
style encyclopaedia_sort_by_button_text is encyclopaedia_button_text:
    size 18

style encyclopaedia_close_button is encyclopaedia_button
style encyclopaedia_close_button_text is encyclopaedia_button_text:
    size 18

# Styles for encyclopaedia_entry screen
style encyclopaedia_entry_frame is encyclopaedia_frame:
    xalign 1.0
    yalign 1.0

    xsize 0.5
    ysize 1.0

    padding (6, 6, 6, 6)

style encyclopaedia_entry_vbox is vbox:
    spacing 6

style encyclopaedia_entry_label_frame is encyclopaedia_frame:
    xalign 1.0
    xfill True

style encyclopaedia_entry_change_entry_frame is encyclopaedia_frame:
    xalign 1.0

style encyclopaedia_entry_content_frame is encyclopaedia_frame:
    left_padding 6
    right_padding 6

    xalign 1.0

style encyclopaedia_entry_image_frame is encyclopaedia_frame:
    xmaximum 0.5
    xalign 0.5
    ymaximum 0.5

style encyclopaedia_entry_change_entry_hbox is hbox:
    xfill True

style encyclopaedia_entry_change_entry_button is button
style encyclopaedia_entry_change_entry_button_text is button_text:
    size 18

style encyclopaedia_entry_page_label:
    size 18
    yalign 0.5

##########################
# Encyclopaedia Misc Setup
##########################
init -85:
    python:
        from itertools import groupby
        from operator import attrgetter
