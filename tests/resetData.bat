del "MockData\GameData\Documents\The Witcher 3\input.settings"
copy "MockData\GameData\Documents\The Witcher 3\input.settings.bak" "MockData\GameData\Documents\The Witcher 3\input.settings"

del "MockData\GameData\Documents\The Witcher 3\user.settings"
copy "MockData\GameData\Documents\The Witcher 3\user.settings.bak" "MockData\GameData\Documents\The Witcher 3\user.settings"

del "MockData\GameData\Documents\The Witcher 3\mods.settings"
copy "MockData\GameData\Documents\The Witcher 3\mods.settings.bak" "MockData\GameData\Documents\The Witcher 3\mods.settings"

del "MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\hidden.xml"
copy "MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\hidden.xml.bak" "MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\hidden.xml"

del "MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\input.xml"
copy "MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\input.xml.bak" "MockData\GameData\Witcher 3\bin\config\r4game\user_config_matrix\pc\input.xml"

del "MockData\GameData\Documents\The Witcher 3 Mod Manager\config.ini"
copy "MockData\GameData\Documents\The Witcher 3 Mod Manager\config.ini.bak" "MockData\GameData\Documents\The Witcher 3 Mod Manager\config.ini"

del /q "MockData\GameData\Witcher 3\mods\*"
for /d %%x in ("Witcher 3\mods\*") do @rd /s /q "%%x"

del /q "MockData\GameData\Witcher 3\dlc\*"
for /d %%x in ("Witcher 3\dlc\*") do @rd /s /q "%%x"
