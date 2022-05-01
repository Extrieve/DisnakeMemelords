import json
import csv
# new_items = [{'anime_id': 49520, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AharenSanWaHakarenai-OP1.webm'}]}, {'anime_id': 49520, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AharenSanWaHakarenai-ED1.webm'}]}, {'anime_id': 49052, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AoAshi-OP1.webm'}]}, {'anime_id': 49052, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AoAshi-ED1.webm'}]}, {'anime_id': 50248, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BirdieWing-OP1.webm'}]}, {'anime_id': 50248, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BirdieWing-ED1.webm'}]}, {'anime_id': 49831, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BlackRockShooterDawnFall-OP1.webm'}]}, {'anime_id': 49831, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BlackRockShooterDawnFall-ED1.webm'}]}, {'anime_id': 48777, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BuildDivideCodeWhite-OP1.webm'}]}, {'anime_id': 48777, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BuildDivideCodeWhite-ED1.webm'}]}, {'anime_id': 51155, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/CapKakumeiBottlemanDX-OP1.webm'}]}, {'anime_id': 48702, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DanceDanceDanseur-OP1.webm'}]}, {'anime_id': 48702, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DanceDanceDanseur-ED1.webm'}]}, {'anime_id': 41461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DateALiveS4-OP1.webm'}]}, {'anime_id': 41461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DateALiveS4-ED1.webm'}]}, {'anime_id': 48779, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Deaimon-OP1.webm'}]}, {'anime_id': 48779, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Deaimon-ED1.webm'}]}, {'anime_id': 50862, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/EstabLife-OP1.webm'}]}, {'anime_id': 50862, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/EstabLife-ED1.webm'}]}, {'anime_id': 48760, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GaikotsuKishi-OP1.webm'}]}, {'anime_id': 48760, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GaikotsuKishi-ED1.webm'}]}, {'anime_id': 49691, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GunjouNoFanfare-OP1.webm'}]}, {'anime_id': 49691, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GunjouNoFanfare-ED1.webm'}]}, {'anime_id': 48857, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HealerGirl-OP1.webm'}]}, {'anime_id': 48857, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HealerGirl-ED1.webm'}]}, {'anime_id': 49692, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HeroineTarumono-OP1.webm'}]}, {'anime_id': 49692, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HeroineTarumono-ED1.webm'}]}, {'anime_id': 42429, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HonzukiNoGekokujouS3-OP1.webm'}]}, {'anime_id': 42429, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HonzukiNoGekokujouS3-ED1.webm'}]}, {'anime_id': 50600, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/InsectLand-ED1.webm'}]}, {'anime_id': 50685, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaginadoS2-ED1.webm'}]}, {'anime_id': 43608, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaguyaSamaWaKokurasetaiS3-OP1.webm'}]}, {'anime_id': 43608, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaguyaSamaWaKokurasetaiS3-ED1.webm'}]}, {'anime_id': 45613, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shikimori-OP1.webm'}]}, {'anime_id': 45613, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shikimori-ED1.webm'}]}, {'anime_id': 50160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KingdomS4-OP1.webm'}]}, {'anime_id': 50160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KingdomS4-ED1.webm'}]}, {'anime_id': 48643, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Koiseka-OP1.webm'}]}, {'anime_id': 48643, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Koiseka-ED1.webm'}]}, {'anime_id': 50631, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KomiSanWaKomyushouDesuS2-OP1.webm'}]}, {'anime_id': 50631, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KomiSanWaKomyushouDesuS2-ED1.webm'}]}, {'anime_id': 48742, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KonoHealerMendokusai-OP1.webm'}]}, {'anime_id': 48742, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KonoHealerMendokusai-ED1.webm'}]},
#              {'anime_id': 50338, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KunoichiTsubaki-OP1.webm'}]}, {'anime_id': 50338, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KunoichiTsubaki-ED1.webm'}]}, {'anime_id': 50678, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KyoukaiSenkiS2-OP1.webm'}]}, {'anime_id': 50678, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KyoukaiSenkiS2-ED1.webm'}]}, {'anime_id': 49556, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveAllPlay-OP1.webm'}]}, {'anime_id': 49556, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveAllPlay-ED1.webm'}]}, {'anime_id': 48916, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveLiveNijigasakiGakuenS2-OP1.webm'}]}, {'anime_id': 48916, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveLiveNijigasakiGakuenS2-ED1.webm'}]}, {'anime_id': 42745, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MachikadoMazokuS2-OP1.webm'}]}, {'anime_id': 42745, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MachikadoMazokuS2-ED1.webm'}]}, {'anime_id': 49291, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MagiaRecordS3-OP1.webm'}]}, {'anime_id': 49291, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MagiaRecordS2-ED1.webm'}]}, {'anime_id': 48842, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MahoutsukaiReimeiki-OP1.webm'}]}, {'anime_id': 48842, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MahoutsukaiReimeiki-ED1.webm'}]}, {'anime_id': 50012, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ZeroNoTeaTime-OP1.webm'}]}, {'anime_id': 50012, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ZeroNoTeaTime-ED1.webm'}]}, {'anime_id': 50955, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Onipan-ED1.webm'}]}, {'anime_id': 50461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Mobseka-OP1.webm'}]}, {'anime_id': 50461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Mobseka-ED1.webm'}]}, {'anime_id': 50380, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ParipiKoumei-OP1.webm'}]}, {'anime_id': 50380, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ParipiKoumei-ED1.webm'}]}, {'anime_id': 48363, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/RPGFudousan-OP1.webm'}]}, {'anime_id': 48363, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/RPGFudousan-ED1.webm'}]}, {'anime_id': 49160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shachisaretai-OP1.webm'}]}, {'anime_id': 49160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shachisaretai-ED1.webm'}]}, {'anime_id': 50060, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShadowverseFlame-OP1.webm'}]}, {'anime_id': 50060, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShadowverseFlame-ED1.webm'}]}, {'anime_id': 48415, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MurabitoA-OP1.webm'}]}, {'anime_id': 48415, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MurabitoA-ED1.webm'}]}, {'anime_id': 47162, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShokeiShoujoNoVirginRoad-OP1.webm'}]}, {'anime_id': 47162, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShokeiShoujoNoVirginRoad-ED1.webm'}]}, {'anime_id': 50265, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/SpyXFamily-OP1.webm'}]}, {'anime_id': 40356, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShieldHeroS2-OP1.webm'}]}, {'anime_id': 40356, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShieldHeroS2-ED1.webm'}]}, {'anime_id': 43693, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ThermaeRomaeNovae-OP1.webm'}]}, {'anime_id': 41595, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TigerAndBunnyS2-OP1.webm'}]}, {'anime_id': 41595, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TigerAndBunnyS2-ED1.webm'}]}, {'anime_id': 50273, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TomodachiGame-OP1.webm'}]}, {'anime_id': 50273, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TomodachiGame-ED1.webm'}]}, {'anime_id': 39935, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/UltramanS2-OP1.webm'}]}, {'anime_id': 39935, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/UltramanS2-ED1.webm'}]}, {'anime_id': 50175, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/YuushaYamemasu-OP1.webm'}]}, {'anime_id': 50175, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/YuushaYamemasu-ED1.webm'}]}]

new_items = [{'mal_id': 49520, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AharenSanWaHakarenai-OP1.webm'}]}, {'mal_id': 49520, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AharenSanWaHakarenai-ED1.webm'}]}, {'mal_id': 49052, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AoAshi-OP1.webm'}]}, {'mal_id': 49052, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/AoAshi-ED1.webm'}]}, {'mal_id': 50248, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BirdieWing-OP1.webm'}]}, {'mal_id': 50248, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BirdieWing-ED1.webm'}]}, {'mal_id': 49831, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BlackRockShooterDawnFall-OP1.webm'}]}, {'mal_id': 49831, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BlackRockShooterDawnFall-ED1.webm'}]}, {'mal_id': 48777, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BuildDivideCodeWhite-OP1.webm'}]}, {'mal_id': 48777, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/BuildDivideCodeWhite-ED1.webm'}]}, {'mal_id': 51155, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/CapKakumeiBottlemanDX-OP1.webm'}]}, {'mal_id': 48702, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DanceDanceDanseur-OP1.webm'}]}, {'mal_id': 48702, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DanceDanceDanseur-ED1.webm'}]}, {'mal_id': 41461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DateALiveS4-OP1.webm'}]}, {'mal_id': 41461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/DateALiveS4-ED1.webm'}]}, {'mal_id': 48779, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Deaimon-OP1.webm'}]}, {'mal_id': 48779, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Deaimon-ED1.webm'}]}, {'mal_id': 50862, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/EstabLife-OP1.webm'}]}, {'mal_id': 50862, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/EstabLife-ED1.webm'}]}, {'mal_id': 48760, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GaikotsuKishi-OP1.webm'}]}, {'mal_id': 48760, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GaikotsuKishi-ED1.webm'}]}, {'mal_id': 49691, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GunjouNoFanfare-OP1.webm'}]}, {'mal_id': 49691, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/GunjouNoFanfare-ED1.webm'}]}, {'mal_id': 48857, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HealerGirl-OP1.webm'}]}, {'mal_id': 48857, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HealerGirl-ED1.webm'}]}, {'mal_id': 49692, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HeroineTarumono-OP1.webm'}]}, {'mal_id': 49692, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HeroineTarumono-ED1.webm'}]}, {'mal_id': 42429, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HonzukiNoGekokujouS3-OP1.webm'}]}, {'mal_id': 42429, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/HonzukiNoGekokujouS3-ED1.webm'}]}, {'mal_id': 50600, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/InsectLand-ED1.webm'}]}, {'mal_id': 50685, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaginadoS2-ED1.webm'}]}, {'mal_id': 43608, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaguyaSamaWaKokurasetaiS3-OP1.webm'}]}, {'mal_id': 43608, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KaguyaSamaWaKokurasetaiS3-ED1.webm'}]}, {'mal_id': 48675, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Cuckoos-OP1.webm'}]}, {'mal_id': 48675, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Cuckoos-ED1.webm'}]}, {'mal_id': 45613, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shikimori-OP1.webm'}]}, {'mal_id': 45613, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shikimori-ED1.webm'}]}, {'mal_id': 50160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KingdomS4-OP1.webm'}]}, {'mal_id': 50160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KingdomS4-ED1.webm'}]}, {'mal_id': 48643, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Koiseka-OP1.webm'}]}, {'mal_id': 48643, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Koiseka-ED1.webm'}]}, {'mal_id': 50631, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KomiSanWaKomyushouDesuS2-OP1.webm'}]}, {'mal_id': 50631, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KomiSanWaKomyushouDesuS2-ED1.webm'}]}, {'mal_id': 48742, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KonoHealerMendokusai-OP1.webm'}]}, {'mal_id': 48742, 'mirrors': [
    {'mirror': 'https://staging.animethemes.moe/video/KonoHealerMendokusai-ED1.webm'}]}, {'mal_id': 50338, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KunoichiTsubaki-OP1.webm'}]}, {'mal_id': 50338, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KunoichiTsubaki-ED1.webm'}]}, {'mal_id': 50678, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KyoukaiSenkiS2-OP1.webm'}]}, {'mal_id': 50678, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/KyoukaiSenkiS2-ED1.webm'}]}, {'mal_id': 49556, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveAllPlay-OP1.webm'}]}, {'mal_id': 49556, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveAllPlay-ED1.webm'}]}, {'mal_id': 48916, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveLiveNijigasakiGakuenS2-OP1.webm'}]}, {'mal_id': 48916, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/LoveLiveNijigasakiGakuenS2-ED1.webm'}]}, {'mal_id': 42745, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MachikadoMazokuS2-OP1.webm'}]}, {'mal_id': 42745, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MachikadoMazokuS2-ED1.webm'}]}, {'mal_id': 49291, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MagiaRecordS3-OP1.webm'}]}, {'mal_id': 49291, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MagiaRecordS2-ED1.webm'}]}, {'mal_id': 48842, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MahoutsukaiReimeiki-OP1.webm'}]}, {'mal_id': 48842, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MahoutsukaiReimeiki-ED1.webm'}]}, {'mal_id': 50012, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ZeroNoTeaTime-OP1.webm'}]}, {'mal_id': 50012, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ZeroNoTeaTime-ED1.webm'}]}, {'mal_id': 50955, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Onipan-ED1.webm'}]}, {'mal_id': 50461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Mobseka-OP1.webm'}]}, {'mal_id': 50461, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Mobseka-ED1.webm'}]}, {'mal_id': 50380, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ParipiKoumei-OP1.webm'}]}, {'mal_id': 50380, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ParipiKoumei-ED1.webm'}]}, {'mal_id': 48363, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/RPGFudousan-OP1.webm'}]}, {'mal_id': 48363, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/RPGFudousan-ED1.webm'}]}, {'mal_id': 49160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shachisaretai-OP1.webm'}]}, {'mal_id': 49160, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/Shachisaretai-ED1.webm'}]}, {'mal_id': 50060, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShadowverseFlame-OP1.webm'}]}, {'mal_id': 50060, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShadowverseFlame-ED1.webm'}]}, {'mal_id': 48415, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MurabitoA-OP1.webm'}]}, {'mal_id': 48415, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/MurabitoA-ED1.webm'}]}, {'mal_id': 47162, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShokeiShoujoNoVirginRoad-OP1.webm'}]}, {'mal_id': 47162, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShokeiShoujoNoVirginRoad-ED1.webm'}]}, {'mal_id': 50265, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/SpyXFamily-OP1.webm'}]}, {'mal_id': 50265, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/SpyXFamily-ED1.webm'}]}, {'mal_id': 40356, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShieldHeroS2-OP1.webm'}]}, {'mal_id': 40356, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ShieldHeroS2-ED1.webm'}]}, {'mal_id': 43693, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/ThermaeRomaeNovae-OP1.webm'}]}, {'mal_id': 41595, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TigerAndBunnyS2-OP1.webm'}]}, {'mal_id': 41595, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TigerAndBunnyS2-ED1.webm'}]}, {'mal_id': 50273, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TomodachiGame-OP1.webm'}]}, {'mal_id': 50273, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/TomodachiGame-ED1.webm'}]}, {'mal_id': 39935, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/UltramanS2-OP1.webm'}]}, {'mal_id': 39935, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/UltramanS2-ED1.webm'}]}, {'mal_id': 50175, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/YuushaYamemasu-OP1.webm'}]}, {'mal_id': 50175, 'mirrors': [{'mirror': 'https://staging.animethemes.moe/video/YuushaYamemasu-ED1.webm'}]}]

# read csv file
available = list(csv.reader(open('registered_ids.csv', 'r')))

for entry in new_items:
    anime_id = entry['anime_id']
    if anime_id not in available:
        print(anime_id)
        available.append(anime_id)

# save csv file
with open('registered_ids1.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(available)

# with open('themes1.json', 'r', encoding='utf-8') as f:
#     themes_data = json.load(f)


# # append new_items to themes_data
# for new_item in new_items:
#     themes_data.append(new_item)

# # save themes_data to themes.json
# with open('themes2.json', 'w', encoding='utf-8') as f:
#     json.dump(themes_data, f, ensure_ascii=False, indent=4)