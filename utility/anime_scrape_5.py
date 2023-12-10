import csv
# new_items = [{'anime_id': 49520, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AharenSanWaHakarenai-OP1.webm'}]}, {'anime_id': 49520, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AharenSanWaHakarenai-ED1.webm'}]}, {'anime_id': 49052, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AoAshi-OP1.webm'}]}, {'anime_id': 49052, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AoAshi-ED1.webm'}]}, {'anime_id': 50248, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BirdieWing-OP1.webm'}]}, {'anime_id': 50248, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BirdieWing-ED1.webm'}]}, {'anime_id': 49831, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BlackRockShooterDawnFall-OP1.webm'}]}, {'anime_id': 49831, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BlackRockShooterDawnFall-ED1.webm'}]}, {'anime_id': 48777, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BuildDivideCodeWhite-OP1.webm'}]}, {'anime_id': 48777, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BuildDivideCodeWhite-ED1.webm'}]}, {'anime_id': 51155, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/CapKakumeiBottlemanDX-OP1.webm'}]}, {'anime_id': 48702, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DanceDanceDanseur-OP1.webm'}]}, {'anime_id': 48702, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DanceDanceDanseur-ED1.webm'}]}, {'anime_id': 41461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DateALiveS4-OP1.webm'}]}, {'anime_id': 41461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DateALiveS4-ED1.webm'}]}, {'anime_id': 48779, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Deaimon-OP1.webm'}]}, {'anime_id': 48779, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Deaimon-ED1.webm'}]}, {'anime_id': 50862, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/EstabLife-OP1.webm'}]}, {'anime_id': 50862, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/EstabLife-ED1.webm'}]}, {'anime_id': 48760, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GaikotsuKishi-OP1.webm'}]}, {'anime_id': 48760, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GaikotsuKishi-ED1.webm'}]}, {'anime_id': 49691, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GunjouNoFanfare-OP1.webm'}]}, {'anime_id': 49691, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GunjouNoFanfare-ED1.webm'}]}, {'anime_id': 48857, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HealerGirl-OP1.webm'}]}, {'anime_id': 48857, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HealerGirl-ED1.webm'}]}, {'anime_id': 49692, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HeroineTarumono-OP1.webm'}]}, {'anime_id': 49692, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HeroineTarumono-ED1.webm'}]}, {'anime_id': 42429, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HonzukiNoGekokujouS3-OP1.webm'}]}, {'anime_id': 42429, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HonzukiNoGekokujouS3-ED1.webm'}]}, {'anime_id': 50600, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/InsectLand-ED1.webm'}]}, {'anime_id': 50685, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaginadoS2-ED1.webm'}]}, {'anime_id': 43608, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaguyaSamaWaKokurasetaiS3-OP1.webm'}]}, {'anime_id': 43608, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaguyaSamaWaKokurasetaiS3-ED1.webm'}]}, {'anime_id': 45613, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shikimori-OP1.webm'}]}, {'anime_id': 45613, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shikimori-ED1.webm'}]}, {'anime_id': 50160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KingdomS4-OP1.webm'}]}, {'anime_id': 50160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KingdomS4-ED1.webm'}]}, {'anime_id': 48643, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Koiseka-OP1.webm'}]}, {'anime_id': 48643, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Koiseka-ED1.webm'}]}, {'anime_id': 50631, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KomiSanWaKomyushouDesuS2-OP1.webm'}]}, {'anime_id': 50631, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KomiSanWaKomyushouDesuS2-ED1.webm'}]}, {'anime_id': 48742, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KonoHealerMendokusai-OP1.webm'}]}, {'anime_id': 48742, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KonoHealerMendokusai-ED1.webm'}]},
#              {'anime_id': 50338, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KunoichiTsubaki-OP1.webm'}]}, {'anime_id': 50338, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KunoichiTsubaki-ED1.webm'}]}, {'anime_id': 50678, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KyoukaiSenkiS2-OP1.webm'}]}, {'anime_id': 50678, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KyoukaiSenkiS2-ED1.webm'}]}, {'anime_id': 49556, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveAllPlay-OP1.webm'}]}, {'anime_id': 49556, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveAllPlay-ED1.webm'}]}, {'anime_id': 48916, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveLiveNijigasakiGakuenS2-OP1.webm'}]}, {'anime_id': 48916, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveLiveNijigasakiGakuenS2-ED1.webm'}]}, {'anime_id': 42745, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MachikadoMazokuS2-OP1.webm'}]}, {'anime_id': 42745, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MachikadoMazokuS2-ED1.webm'}]}, {'anime_id': 49291, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MagiaRecordS3-OP1.webm'}]}, {'anime_id': 49291, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MagiaRecordS2-ED1.webm'}]}, {'anime_id': 48842, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MahoutsukaiReimeiki-OP1.webm'}]}, {'anime_id': 48842, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MahoutsukaiReimeiki-ED1.webm'}]}, {'anime_id': 50012, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ZeroNoTeaTime-OP1.webm'}]}, {'anime_id': 50012, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ZeroNoTeaTime-ED1.webm'}]}, {'anime_id': 50955, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Onipan-ED1.webm'}]}, {'anime_id': 50461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Mobseka-OP1.webm'}]}, {'anime_id': 50461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Mobseka-ED1.webm'}]}, {'anime_id': 50380, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ParipiKoumei-OP1.webm'}]}, {'anime_id': 50380, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ParipiKoumei-ED1.webm'}]}, {'anime_id': 48363, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/RPGFudousan-OP1.webm'}]}, {'anime_id': 48363, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/RPGFudousan-ED1.webm'}]}, {'anime_id': 49160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shachisaretai-OP1.webm'}]}, {'anime_id': 49160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shachisaretai-ED1.webm'}]}, {'anime_id': 50060, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShadowverseFlame-OP1.webm'}]}, {'anime_id': 50060, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShadowverseFlame-ED1.webm'}]}, {'anime_id': 48415, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MurabitoA-OP1.webm'}]}, {'anime_id': 48415, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MurabitoA-ED1.webm'}]}, {'anime_id': 47162, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShokeiShoujoNoVirginRoad-OP1.webm'}]}, {'anime_id': 47162, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShokeiShoujoNoVirginRoad-ED1.webm'}]}, {'anime_id': 50265, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/SpyXFamily-OP1.webm'}]}, {'anime_id': 40356, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShieldHeroS2-OP1.webm'}]}, {'anime_id': 40356, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShieldHeroS2-ED1.webm'}]}, {'anime_id': 43693, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ThermaeRomaeNovae-OP1.webm'}]}, {'anime_id': 41595, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TigerAndBunnyS2-OP1.webm'}]}, {'anime_id': 41595, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TigerAndBunnyS2-ED1.webm'}]}, {'anime_id': 50273, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TomodachiGame-OP1.webm'}]}, {'anime_id': 50273, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TomodachiGame-ED1.webm'}]}, {'anime_id': 39935, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/UltramanS2-OP1.webm'}]}, {'anime_id': 39935, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/UltramanS2-ED1.webm'}]}, {'anime_id': 50175, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/YuushaYamemasu-OP1.webm'}]}, {'anime_id': 50175, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/YuushaYamemasu-ED1.webm'}]}]

# new_items = [{'mal_id': 49520, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AharenSanWaHakarenai-OP1.webm'}]}, {'mal_id': 49520, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AharenSanWaHakarenai-ED1.webm'}]}, {'mal_id': 49052, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AoAshi-OP1.webm'}]}, {'mal_id': 49052, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AoAshi-ED1.webm'}]}, {'mal_id': 50248, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BirdieWing-OP1.webm'}]}, {'mal_id': 50248, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BirdieWing-ED1.webm'}]}, {'mal_id': 49831, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BlackRockShooterDawnFall-OP1.webm'}]}, {'mal_id': 49831, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BlackRockShooterDawnFall-ED1.webm'}]}, {'mal_id': 48777, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BuildDivideCodeWhite-OP1.webm'}]}, {'mal_id': 48777, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BuildDivideCodeWhite-ED1.webm'}]}, {'mal_id': 51155, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/CapKakumeiBottlemanDX-OP1.webm'}]}, {'mal_id': 48702, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DanceDanceDanseur-OP1.webm'}]}, {'mal_id': 48702, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DanceDanceDanseur-ED1.webm'}]}, {'mal_id': 41461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DateALiveS4-OP1.webm'}]}, {'mal_id': 41461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DateALiveS4-ED1.webm'}]}, {'mal_id': 48779, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Deaimon-OP1.webm'}]}, {'mal_id': 48779, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Deaimon-ED1.webm'}]}, {'mal_id': 50862, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/EstabLife-OP1.webm'}]}, {'mal_id': 50862, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/EstabLife-ED1.webm'}]}, {'mal_id': 48760, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GaikotsuKishi-OP1.webm'}]}, {'mal_id': 48760, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GaikotsuKishi-ED1.webm'}]}, {'mal_id': 49691, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GunjouNoFanfare-OP1.webm'}]}, {'mal_id': 49691, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GunjouNoFanfare-ED1.webm'}]}, {'mal_id': 48857, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HealerGirl-OP1.webm'}]}, {'mal_id': 48857, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HealerGirl-ED1.webm'}]}, {'mal_id': 49692, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HeroineTarumono-OP1.webm'}]}, {'mal_id': 49692, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HeroineTarumono-ED1.webm'}]}, {'mal_id': 42429, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HonzukiNoGekokujouS3-OP1.webm'}]}, {'mal_id': 42429, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HonzukiNoGekokujouS3-ED1.webm'}]}, {'mal_id': 50600, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/InsectLand-ED1.webm'}]}, {'mal_id': 50685, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaginadoS2-ED1.webm'}]}, {'mal_id': 43608, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaguyaSamaWaKokurasetaiS3-OP1.webm'}]}, {'mal_id': 43608, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaguyaSamaWaKokurasetaiS3-ED1.webm'}]}, {'mal_id': 48675, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Cuckoos-OP1.webm'}]}, {'mal_id': 48675, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Cuckoos-ED1.webm'}]}, {'mal_id': 45613, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shikimori-OP1.webm'}]}, {'mal_id': 45613, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shikimori-ED1.webm'}]}, {'mal_id': 50160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KingdomS4-OP1.webm'}]}, {'mal_id': 50160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KingdomS4-ED1.webm'}]}, {'mal_id': 48643, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Koiseka-OP1.webm'}]}, {'mal_id': 48643, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Koiseka-ED1.webm'}]}, {'mal_id': 50631, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KomiSanWaKomyushouDesuS2-OP1.webm'}]}, {'mal_id': 50631, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KomiSanWaKomyushouDesuS2-ED1.webm'}]}, {'mal_id': 48742, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KonoHealerMendokusai-OP1.webm'}]}, {'mal_id': 48742, 'mirrors': [
#     {'mirror': 'https://staging.animethemes.moe/video/KonoHealerMendokusai-ED1.webm'}]}, {'mal_id': 50338, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KunoichiTsubaki-OP1.webm'}]}, {'mal_id': 50338, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KunoichiTsubaki-ED1.webm'}]}, {'mal_id': 50678, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KyoukaiSenkiS2-OP1.webm'}]}, {'mal_id': 50678, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KyoukaiSenkiS2-ED1.webm'}]}, {'mal_id': 49556, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveAllPlay-OP1.webm'}]}, {'mal_id': 49556, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveAllPlay-ED1.webm'}]}, {'mal_id': 48916, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveLiveNijigasakiGakuenS2-OP1.webm'}]}, {'mal_id': 48916, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveLiveNijigasakiGakuenS2-ED1.webm'}]}, {'mal_id': 42745, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MachikadoMazokuS2-OP1.webm'}]}, {'mal_id': 42745, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MachikadoMazokuS2-ED1.webm'}]}, {'mal_id': 49291, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MagiaRecordS3-OP1.webm'}]}, {'mal_id': 49291, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MagiaRecordS2-ED1.webm'}]}, {'mal_id': 48842, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MahoutsukaiReimeiki-OP1.webm'}]}, {'mal_id': 48842, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MahoutsukaiReimeiki-ED1.webm'}]}, {'mal_id': 50012, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ZeroNoTeaTime-OP1.webm'}]}, {'mal_id': 50012, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ZeroNoTeaTime-ED1.webm'}]}, {'mal_id': 50955, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Onipan-ED1.webm'}]}, {'mal_id': 50461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Mobseka-OP1.webm'}]}, {'mal_id': 50461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Mobseka-ED1.webm'}]}, {'mal_id': 50380, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ParipiKoumei-OP1.webm'}]}, {'mal_id': 50380, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ParipiKoumei-ED1.webm'}]}, {'mal_id': 48363, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/RPGFudousan-OP1.webm'}]}, {'mal_id': 48363, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/RPGFudousan-ED1.webm'}]}, {'mal_id': 49160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shachisaretai-OP1.webm'}]}, {'mal_id': 49160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shachisaretai-ED1.webm'}]}, {'mal_id': 50060, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShadowverseFlame-OP1.webm'}]}, {'mal_id': 50060, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShadowverseFlame-ED1.webm'}]}, {'mal_id': 48415, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MurabitoA-OP1.webm'}]}, {'mal_id': 48415, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MurabitoA-ED1.webm'}]}, {'mal_id': 47162, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShokeiShoujoNoVirginRoad-OP1.webm'}]}, {'mal_id': 47162, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShokeiShoujoNoVirginRoad-ED1.webm'}]}, {'mal_id': 50265, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/SpyXFamily-OP1.webm'}]}, {'mal_id': 50265, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/SpyXFamily-ED1.webm'}]}, {'mal_id': 40356, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShieldHeroS2-OP1.webm'}]}, {'mal_id': 40356, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShieldHeroS2-ED1.webm'}]}, {'mal_id': 43693, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ThermaeRomaeNovae-OP1.webm'}]}, {'mal_id': 41595, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TigerAndBunnyS2-OP1.webm'}]}, {'mal_id': 41595, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TigerAndBunnyS2-ED1.webm'}]}, {'mal_id': 50273, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TomodachiGame-OP1.webm'}]}, {'mal_id': 50273, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TomodachiGame-ED1.webm'}]}, {'mal_id': 39935, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/UltramanS2-OP1.webm'}]}, {'mal_id': 39935, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/UltramanS2-ED1.webm'}]}, {'mal_id': 50175, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/YuushaYamemasu-OP1.webm'}]}, {'mal_id': 50175, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/YuushaYamemasu-ED1.webm'}]}]


new_items = [{'anime_id': 49599, 'mirrors': [{'mirror': 'https://v.animethemes.moe/AniNiTsukeruS5-OP1.webm'}]}, {'anime_id': 51989, 'mirrors': [{'mirror': 'https://v.animethemes.moe/BangDreamMorfonication-ED1.webm'}]}, {'anime_id': 51989, 'mirrors': [{'mirror': 'https://v.animethemes.moe/BangDreamMorfonication-ED2.webm'}]}, {'anime_id': 50953, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Bastard2022-OP1.webm'}]}, {'anime_id': 50953, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Bastard2022-ED1.webm'}]}, {'anime_id': 51371, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Bucchigire-OP1.webm'}]}, {'anime_id': 51371, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Bucchigire-OP1v2.webm'}]}, {'anime_id': 51371, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Bucchigire-ED1.webm'}]}, {'anime_id': 49819, 'mirrors': [{'mirror': 'https://v.animethemes.moe/CardfightVanguardWillDress-OP1.webm'}]}, {'anime_id': 49819, 'mirrors': [{'mirror': 'https://v.animethemes.moe/CardfightVanguardWillDress-ED1.webm'}]}, {'anime_id': 50985, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Chimimo-OP1.webm'}]}, {'anime_id': 50985, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Chimimo-ED1.webm'}]}, {'anime_id': 50612, 'mirrors': [{'mirror': 'https://v.animethemes.moe/DrStoneRyuusui-OP1.webm'}]}, {'anime_id': 47164, 'mirrors': [{'mirror': 'https://v.animethemes.moe/DanMachiS4-OP1.webm'}]}, {'anime_id': 47164, 'mirrors': [{'mirror': 'https://v.animethemes.moe/DanMachiS4-ED1.webm'}]}, {'anime_id': 51417, 'mirrors': [{'mirror': 'https://v.animethemes.moe/EngageKiss-OP1.webm'}]}, {'anime_id': 51417, 'mirrors': [{'mirror': 'https://v.animethemes.moe/EngageKiss-OP1v2.webm'}]}, {'anime_id': 51417, 'mirrors': [{'mirror': 'https://v.animethemes.moe/EngageKiss-ED1.webm'}]}, {'anime_id': 50999, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ExtremeHearts-OP1.webm'}]}, {'anime_id': 50999, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ExtremeHearts-ED1.webm'}]}, {'anime_id': 50999, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ExtremeHearts-ED2.webm'}]}, {'anime_id': 50999, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ExtremeHearts-ED2v2.webm'}]}, {'anime_id': 50999, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ExtremeHearts-ED3.webm'}]}, {'anime_id': 50999, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ExtremeHearts-ED4.webm'}]}, {'anime_id': 50999, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ExtremeHearts-ED4v2.webm'}]}, {'anime_id': 50999, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ExtremeHearts-ED4v3.webm'}]}, {'anime_id': 48649, 'mirrors': [{'mirror': 'https://v.animethemes.moe/FuutoTantei-OP1.webm'}]}, {'anime_id': 48649, 'mirrors': [{'mirror': 'https://v.animethemes.moe/FuutoTantei-ED1.webm'}]}, {'anime_id': 49551, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HanabiChanWaOkuregachi-OP1.webm'}]}, {'anime_id': 49551, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HanabiChanWaOkuregachi-OP2.webm'}]}, {'anime_id': 49551, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HanabiChanWaOkuregachi-OP3.webm'}]}, {'anime_id': 49551, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HanabiChanWaOkuregachi-OP4.webm'}]}, {'anime_id': 49551, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HanabiChanWaOkuregachi-OP5.webm'}]}, {'anime_id': 49551, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HanabiChanWaOkuregachi-OP6.webm'}]}, {'anime_id': 49551, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HanabiChanWaOkuregachi-ED1.webm'}]}, {'anime_id': 48413, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HatarakuMaouSamaS2-OP1.webm'}]}, {'anime_id': 48413, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HatarakuMaouSamaS2-ED1.webm'}]}, {'anime_id': 50891, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HoshiNoSamidare-OP1.webm'}]}, {'anime_id': 50891, 'mirrors': [{'mirror': 'https://v.animethemes.moe/HoshiNoSamidare-ED1.webm'}]}, {'anime_id': 44524, 'mirrors': [{'mirror': 'https://v.animethemes.moe/IsekaiHarem-OP1.webm'}]}, {'anime_id': 44524, 'mirrors': [{'mirror': 'https://v.animethemes.moe/IsekaiHarem-ED1.webm'}]}, {'anime_id': 49220, 'mirrors': [{'mirror': 'https://v.animethemes.moe/IsekaiOjisan-OP1.webm'}]}, {'anime_id': 49220, 'mirrors': [{'mirror': 'https://v.animethemes.moe/IsekaiOjisan-ED1.webm'}]}, {'anime_id': 49438, 'mirrors': [{'mirror': 'https://v.animethemes.moe/IsekaiYakkyoku-OP1.webm'}]}, {'anime_id': 49438, 'mirrors': [{'mirror': 'https://v.animethemes.moe/IsekaiYakkyoku-ED1.webm'}]}, {'anime_id': 42994, 'mirrors': [{'mirror': 'https://v.animethemes.moe/JashinChanDropkickS3-OP1.webm'}]}, {'anime_id': 42994, 'mirrors': [{'mirror': 'https://v.animethemes.moe/JashinChanDropkickS3-ED1.webm'}]}, {'anime_id': 42994, 'mirrors': [{'mirror': 'https://v.animethemes.moe/JashinChanDropkickS3-ED2.webm'}]}, {'anime_id': 50339, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KakeguruiTwin-OP1.webm'}]}, {'anime_id': 50339, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KakeguruiTwin-ED1.webm'}]}, {'anime_id': 50470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KamiKuzuIdol-OP1.webm'}]}, {'anime_id': 50470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KamiKuzuIdol-ED1.webm'}]}, {'anime_id': 50470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KamiKuzuIdol-ED2.webm'}]}, {'anime_id': 50470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KamiKuzuIdol-ED3.webm'}]}, {'anime_id': 50470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KamiKuzuIdol-ED4.webm'}]}, {'anime_id': 50470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KamiKuzuIdol-ED5.webm'}]}, {'anime_id': 50470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KamiKuzuIdol-ED6.webm'}]}, {'anime_id': 50470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KamiKuzuIdol-ED7.webm'}]}, {'anime_id': 42963, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KanokariS2-OP1.webm'}]}, {'anime_id': 42963, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KanokariS2-ED1.webm'}]}, {'anime_id': 51213, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KinsouNoVermeil-OP1.webm'}]}, {'anime_id': 51213, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KinsouNoVermeil-ED1.webm'}]}, {'anime_id': 51773, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KJFile-ED1.webm'}]}, {'anime_id': 52273, 'mirrors': [{'mirror': 'https://v.animethemes.moe/SaintSeiyaBattleForSanctuary-OP1.webm'}]}, {'anime_id': 52273, 'mirrors': [{'mirror': 'https://v.animethemes.moe/SaintSeiya2019-ED1.webm'}]}, {'anime_id': 49776, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KumichouMusume-OP1.webm'}]}, {'anime_id': 49776, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KumichouMusume-ED1.webm'}]}, {'anime_id': 51064, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KuroNoShoukanshi-OP1.webm'}]}, {'anime_id': 51064, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KuroNoShoukanshi-OP1v2.webm'}]}, {'anime_id': 51064, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KuroNoShoukanshi-ED1.webm'}]}, {'anime_id': 51064, 'mirrors': [{'mirror': 'https://v.animethemes.moe/KuroNoShoukanshi-ED2.webm'}]}, {'anime_id': 50203, 'mirrors': [{'mirror': 'https://v.animethemes.moe/LoveLiveSuperstarS2-OP1.webm'}]}, {'anime_id': 50203, 'mirrors': [{'mirror': 'https://v.animethemes.moe/LoveLiveSuperstarS2-ED1.webm'}]}, {'anime_id': 50203, 'mirrors': [{'mirror': 'https://v.animethemes.moe/LoveLiveSuperstarS2-ED2.webm'}]}, {'anime_id': 50203, 'mirrors': [{'mirror': 'https://v.animethemes.moe/LoveLiveSuperstarS2-ED3.webm'}]}, {'anime_id': 50203, 'mirrors': [{'mirror': 'https://v.animethemes.moe/LoveLiveSuperstarS2-ED4.webm'}]}, {'anime_id': 50203, 'mirrors': [{'mirror': 'https://v.animethemes.moe/LoveLiveSuperstarS2-ED5.webm'}]}, {'anime_id': 50203, 'mirrors': [{'mirror': 'https://v.animethemes.moe/LoveLiveSuperstarS2-ED6.webm'}]}, {'anime_id': 50203, 'mirrors': [{'mirror': 'https://v.animethemes.moe/LoveLiveSuperstarS2-ED7.webm'}]}, {'anime_id': 50709, 'mirrors': [{'mirror': 'https://v.animethemes.moe/LycorisRecoil-OP1.webm'}]}, {'anime_id': 50709, 'mirrors': [{'mirror':'https://v.animethemes.moe/LycorisRecoil-ED1.webm'}]}, {'anime_id': 41084, 'mirrors': [{'mirror': 'https://v.animethemes.moe/MadeInAbyssS2-OP1.webm'}]}, {'anime_id': 41084, 'mirrors': [{'mirror': 'https://v.animethemes.moe/MadeInAbyssS2-OP2.webm'}]}, {'anime_id': 41084, 'mirrors': [{'mirror': 'https://v.animethemes.moe/MadeInAbyssS2-ED1.webm'}]}, {'anime_id': 49470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Tsurekano-OP1.webm'}]}, {'anime_id': 49470, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Tsurekano-ED1.webm'}]}, {'anime_id': 52045, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ObeyMeS2-ED1.webm'}]}, {'anime_id': 51368, 'mirrors': [{'mirror': 'https://v.animethemes.moe/OrientPart2-OP1.webm'}]}, {'anime_id': 51368, 'mirrors': [{'mirror': 'https://v.animethemes.moe/OrientPart2-ED1.webm'}]}, {'anime_id': 48895, 'mirrors': [{'mirror': 'https://v.animethemes.moe/OverlordS4-OP1.webm'}]}, {'anime_id': 48895, 'mirrors': [{'mirror': 'https://v.animethemes.moe/OverlordS4-ED1.webm'}]}, {'anime_id': 50917, 'mirrors': [{'mirror': 'https://v.animethemes.moe/PrimaDoll-OP1.webm'}]}, {'anime_id': 50917, 'mirrors': [{'mirror': 'https://v.animethemes.moe/PrimaDoll-ED1.webm'}]}, {'anime_id': 50917,'mirrors': [{'mirror': 'https://v.animethemes.moe/PrimaDoll-ED2.webm'}]}, {'anime_id': 50917, 'mirrors': [{'mirror': 'https://v.animethemes.moe/PrimaDoll-ED3.webm'}]}, {'anime_id': 50917, 'mirrors': [{'mirror': 'https://v.animethemes.moe/PrimaDoll-ED4.webm'}]}, {'anime_id': 50917, 'mirrors': [{'mirror': 'https://v.animethemes.moe/PrimaDoll-ED5.webm'}]}, {'anime_id': 50917, 'mirrors': [{'mirror': 'https://v.animethemes.moe/PrimaDoll-ED6.webm'}]}, {'anime_id': 50917, 'mirrors': [{'mirror': 'https://v.animethemes.moe/PrimaDoll-ED7.webm'}]}, {'anime_id': 51381, 'mirrors': [{'mirror': 'https://v.animethemes.moe/RWBYHyousetsuTeikoku-OP1.webm'}]}, {'anime_id': 51381, 'mirrors': [{'mirror': 'https://v.animethemes.moe/RWBYHyousetsuTeikoku-ED1.webm'}]}, {'anime_id': 51381, 'mirrors': [{'mirror': 'https://v.animethemes.moe/RWBYHyousetsuTeikoku-ED1v2.webm'}]}, {'anime_id': 51837, 'mirrors': [{'mirror': 'https://v.animethemes.moe/SaikinYatottaMaidGaAyashii-OP1.webm'}]}, {'anime_id': 51837, 'mirrors': [{'mirror': 'https://v.animethemes.moe/SaikinYatottaMaidGaAyashii-ED1.webm'}]}, {'anime_id': 49782, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ShadowsHouseS2-OP1.webm'}]}, {'anime_id': 49782, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ShadowsHouseS2-ED1.webm'}]}, {'anime_id': 50221, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ShinePost-OP1.webm'}]}, {'anime_id': 50221, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ShinePost-ED1.webm'}]}, {'anime_id': 50221, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ShinePost-ED2.webm'}]}, {'anime_id': 50221, 'mirrors': [{'mirror': 'https://v.animethemes.moe/ShinePost-ED3.webm'}]}, {'anime_id': 45653, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Soreayu-OP1.webm'}]}, {'anime_id': 45653, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Soreayu-ED1.webm'}]}, {'anime_id': 50760, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Teppen-OP1.webm'}]}, {'anime_id': 50760,'mirrors': [{'mirror': 'https://v.animethemes.moe/Teppen-ED1.webm'}]}, {'anime_id': 50760, 'mirrors': [{'mirror': 'https://v.animethemes.moe/Teppen-ED2.webm'}]}, {'anime_id': 41589, 'mirrors': [{'mirror': 'https://v.animethemes.moe/TokyoMewMewNew-OP1.webm'}]}, {'anime_id': 41589, 'mirrors': [{'mirror': 'https://v.animethemes.moe/TokyoMewMewNew-ED1.webm'}]}, {'anime_id': 40590, 'mirrors': [{'mirror': 'https://v.animethemes.moe/UtawarerumonoFutariNoHakuoro-OP1.webm'}]}, {'anime_id': 40590, 'mirrors': [{'mirror': 'https://v.animethemes.moe/UtawarerumonoFutariNoHakuoro-ED1.webm'}]}, {'anime_id': 40590, 'mirrors': [{'mirror': 'https://v.animethemes.moe/UtawarerumonoFutariNoHakuoro-ED2.webm'}]}, {'anime_id': 51923, 'mirrors': [{'mirror': 'https://v.animethemes.moe/WarauArsnotoriaSun-OP1.webm'}]}, {'anime_id': 51923, 'mirrors': [{'mirror': 'https://v.animethemes.moe/WarauArsnotoriaSun-ED1.webm'}]}, {'anime_id': 50346, 'mirrors': [{'mirror': 'https://v.animethemes.moe/YofukashiNoUta-OP1.webm'}]}, {'anime_id': 50346, 'mirrors': [{'mirror': 'https://v.animethemes.moe/YofukashiNoUta-OP1-BD1080.webm'}]}, {'anime_id': 50346, 'mirrors': [{'mirror': 'https://v.animethemes.moe/YofukashiNoUta-ED1.webm'}]}, {'anime_id': 50346, 'mirrors': [{'mirror': 'https://v.animethemes.moe/YofukashiNoUta-ED1-NCBD1080.webm'}]}, {'anime_id': 51096, 'mirrors': [{'mirror': 'https://v.animethemes.moe/YoukosoZitsuS2-OP1.webm'}]}, {'anime_id': 51096, 'mirrors': [{'mirror': 'https://v.animethemes.moe/YoukosoZitsuS2-ED1.webm'}]}, {'anime_id': 51092, 'mirrors': [{'mirror': 'https://v.animethemes.moe/YureiDeco-OP1.webm'}]}, {'anime_id': 51092, 'mirrors': [{'mirror': 'https://v.animethemes.moe/YureiDeco-OP1v2.webm'}]}, {'anime_id': 51092, 'mirrors': [{'mirror': 'https://v.animethemes.moe/YureiDeco-ED1.webm'}]}, {'anime_id': 51092, 'mirrors':[{'mirror': 'https://v.animethemes.moe/YureiDeco-ED1v2.webm'}]}]

# read csv file
available = list(csv.reader(open('db/registered_ids3.csv', 'r')))

for entry in new_items:
    anime_id = entry['anime_id']
    if anime_id not in available:
        available.append([anime_id])

# save csv file
with open('db/registered_ids4.csv', 'w', encoding='utf-8', newline='\n') as f:
    writer = csv.writer(f)
    # Write every int in the list as a row in the csv file
    writer.writerows(available)



# with open('themes1.json', 'r', encoding='utf-8') as f:
#     themes_data = json.load(f)


# # append new_items to themes_data
# for new_item in new_items:
#     themes_data.append(new_item)

# # save themes_data to themes.json
# with open('themes2.json', 'w', encoding='utf-8') as f:
#     json.dump(themes_data, f, ensure_ascii=False, indent=4)