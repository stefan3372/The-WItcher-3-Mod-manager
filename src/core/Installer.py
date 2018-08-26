from src.core.Fetcher import Fetcher


class Installer:
    active = []
    fetcher = Fetcher()

    def install(self):
        for modPath in self.active:
            mod = self.fetcher.fetch(modPath)
            # mod.installXmlKeys()
            # mod.installInputKeys(ui)
            # mod.installUserSettings()
            # mod.loadPriority()

            # add to existing
            # exists = False
            # for installed in ui.modList.values():
            #     if (mod.files == installed.files):
            #         installed.usersettings = mod.usersettings
            #         installed.hidden = mod.hidden
            #         installed.xmlkeys = mod.xmlkeys
            #         installed.dlcs = mod.dlcs
            #         installed.date = mod.date
            #         installed.menus = mod.menus
            #         installed.inputsettings = mod.inputsettings
            #         exists = True
            #         break
            # if (not exists):
            #     ui.addMod(mod.name, mod)

    def uninstall(self, mod):
        pass

    def enable(self):
        pass

    def disable(self):
        pass
