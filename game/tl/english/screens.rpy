# TODO: Translation updated at 2022-11-17 21:36

translate english strings:

    # game/screens.rpy:252
    old "Voltar"
    new ""

    # game/screens.rpy:253
    old "History"
    new ""

    # game/screens.rpy:254
    old "Skip"
    new ""

    # game/screens.rpy:255
    old "Auto"
    new ""

    # game/screens.rpy:256
    old "Save"
    new ""

    # game/screens.rpy:257
    old "Q.Save"
    new ""

    # game/screens.rpy:258
    old "Q.Load"
    new ""

    # game/screens.rpy:259
    old "Prefs"
    new ""

    # game/screens.rpy:300
    old "Start"
    new ""

    # game/screens.rpy:308
    old "Load"
    new ""

    # game/screens.rpy:310
    old "Preferences"
    new ""

    # game/screens.rpy:314
    old "End Replay"
    new ""

    # game/screens.rpy:318
    old "Main Menu"
    new ""

    # game/screens.rpy:320
    old "Sobre"
    new ""

    # game/screens.rpy:325
    old "Help"
    new ""

    # game/screens.rpy:331
    old "Sair"
    new ""

    # game/screens.rpy:556
    old "Version [config.version!t]\n"
    new ""

    # game/screens.rpy:562
    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new ""

    # game/screens.rpy:598
    old "Page {}"
    new ""

    # game/screens.rpy:598
    old "Automatic saves"
    new ""

    # game/screens.rpy:598
    old "Quick saves"
    new ""

    # game/screens.rpy:640
    old "{#file_time}%A, %B %d %Y, %H:%M"
    new ""

    # game/screens.rpy:640
    old "empty slot"
    new ""

    # game/screens.rpy:657
    old "<"
    new ""

    # game/screens.rpy:660
    old "{#auto_page}A"
    new ""

    # game/screens.rpy:663
    old "{#quick_page}Q"
    new ""

    # game/screens.rpy:669
    old ">"
    new ""

    # game/screens.rpy:726
    old "Display"
    new ""

    # game/screens.rpy:727
    old "Window"
    new ""

    # game/screens.rpy:728
    old "Fullscreen"
    new ""

    # game/screens.rpy:733
    old "Unseen Text"
    new ""

    # game/screens.rpy:734
    old "After Choices"
    new ""

    # game/screens.rpy:735
    old "Transitions"
    new ""

    # game/screens.rpy:748
    old "Text Speed"
    new ""

    # game/screens.rpy:752
    old "Auto-Forward Time"
    new ""

    # game/screens.rpy:759
    old "Music Volume"
    new ""

    # game/screens.rpy:766
    old "Sound Volume"
    new ""

    # game/screens.rpy:772
    old "Test"
    new ""

    # game/screens.rpy:776
    old "Voice Volume"
    new ""

    # game/screens.rpy:787
    old "Mute All"
    new ""

    # game/screens.rpy:906
    old "The dialogue history is empty."
    new ""

    # game/screens.rpy:974
    old "Keyboard"
    new ""

    # game/screens.rpy:975
    old "Mouse"
    new ""

    # game/screens.rpy:978
    old "Gamepad"
    new ""

    # game/screens.rpy:991
    old "Enter"
    new ""

    # game/screens.rpy:992
    old "Advances dialogue and activates the interface."
    new ""

    # game/screens.rpy:995
    old "Space"
    new ""

    # game/screens.rpy:996
    old "Advances dialogue without selecting choices."
    new ""

    # game/screens.rpy:999
    old "Arrow Keys"
    new ""

    # game/screens.rpy:1000
    old "Navigate the interface."
    new ""

    # game/screens.rpy:1003
    old "Escape"
    new ""

    # game/screens.rpy:1004
    old "Accesses the game menu."
    new ""

    # game/screens.rpy:1007
    old "Ctrl"
    new ""

    # game/screens.rpy:1008
    old "Skips dialogue while held down."
    new ""

    # game/screens.rpy:1011
    old "Tab"
    new ""

    # game/screens.rpy:1012
    old "Toggles dialogue skipping."
    new ""

    # game/screens.rpy:1015
    old "Page Up"
    new ""

    # game/screens.rpy:1016
    old "Rolls back to earlier dialogue."
    new ""

    # game/screens.rpy:1019
    old "Page Down"
    new ""

    # game/screens.rpy:1020
    old "Rolls forward to later dialogue."
    new ""

    # game/screens.rpy:1024
    old "Hides the user interface."
    new ""

    # game/screens.rpy:1028
    old "Takes a screenshot."
    new ""

    # game/screens.rpy:1032
    old "Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}."
    new ""

    # game/screens.rpy:1036
    old "Opens the accessibility menu."
    new ""

    # game/screens.rpy:1042
    old "Left Click"
    new ""

    # game/screens.rpy:1046
    old "Middle Click"
    new ""

    # game/screens.rpy:1050
    old "Right Click"
    new ""

    # game/screens.rpy:1054
    old "Mouse Wheel Up\nClick Rollback Side"
    new ""

    # game/screens.rpy:1058
    old "Mouse Wheel Down"
    new ""

    # game/screens.rpy:1065
    old "Right Trigger\nA/Bottom Button"
    new ""

    # game/screens.rpy:1069
    old "Left Trigger\nLeft Shoulder"
    new ""

    # game/screens.rpy:1073
    old "Right Shoulder"
    new ""

    # game/screens.rpy:1078
    old "D-Pad, Sticks"
    new ""

    # game/screens.rpy:1082
    old "Start, Guide"
    new ""

    # game/screens.rpy:1086
    old "Y/Top Button"
    new ""

    # game/screens.rpy:1089
    old "Calibrate"
    new ""

    # game/screens.rpy:1154
    old "Sim"
    new ""

    # game/screens.rpy:1201
    old "Skipping"
    new ""

    # game/screens.rpy:1424
    old "Menu"
    new ""

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("[config.version!t]\n")

            hbox:
                spacing 15
                text _("Créditos:")

            hbox:
                spacing 15
                text _("Jogo desenvolvido por: Gabriel Salere Brandine; Bruna C. Rodrigues da Cunha")
                text _("\n")

            hbox:
                spacing 15
                text _("Licença: GNU AFFERO GENERAL PUBLIC LICENSE Version 3")
                text _("\n")

            hbox:
                spacing 15
                text _("Artes dos personagens: aplicativo PitzMaker (EIGHT STUDIO)")
                text _("\n")

            hbox:
                spacing 15
                text _("Músicas:")
            
            hbox:
                spacing 15
                text _("Pop Mellow Background Music by Plastic3 is licensed under CC BY-NC-SA 3.0.")
            
            hbox:
                spacing 15
                text _("Business News TV Commercial Background Music by PremiumMusic (Instrumental Version) is licensed under CC BY-NC-ND 3.0.")

            hbox:
                spacing 15
                text _("Funny Comic Detective Playful Comedy Background Music by Eitan Epstein Music is licensed under CC BY-NC-ND 3.0.")

            hbox:
                spacing 15
                text _("Chill Dramatic Cinematic Music by Plastic3 is licensed under CC BY-NC-ND 3.0.")

            hbox:
                spacing 15
                text _("Background Music by corporatemusic is licensed under CC BY-NC-ND 3.0.")

            hbox:
                spacing 15
                text _("Cinematic Motivating Energizing Bass Guitar Background Music Theme 001 by PremiumMusic (Instrumental Version) is licensed under CC BY-NC-ND 3.0. ")

