del "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3\input.settings"
copy "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3\input.settings.bak" "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3\input.settings"

del "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3\user.settings"
copy "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3\user.settings.bak" "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3\user.settings"

del "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3\mods.settings"
copy "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3\mods.settings.bak" "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3\mods.settings"

del "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\hidden.xml"
copy "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\hidden.xml.bak" "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\hidden.xml"

del "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\input.xml"
copy "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\input.xml.bak" "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\input.xml"

del "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3 Mod Manager\config.ini"
copy "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3 Mod Manager\config.ini.bak" "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Documents\The Witcher 3 Mod Manager\config.ini"

del /q "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\mods\*"
for /d %%x in ("C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\mods\*") do @rd /s /q "%%x"

del /q "C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\dlc\*"
for /d %%x in ("C:\Projects\The-WItcher-3-Mod-manager\tests\MockData\GameData\Witcher 3\dlc\*") do @rd /s /q "%%x"