#!/usr/bin/env python36
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright (c) 2018, CJ Kucera
# All rights reserved.
#   
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Good gods, this is a big ol' dict, isn't it?
level_sequence_event_names = {
    'BL2': {
        'sage_powerstation_p': {
        },
        'iris_dl1_tas_p': {
            'iris_closemaindoors': [
                'Iris_DL1_TAS_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'iris_dl1_gasdoor': [
                'Iris_DL1_TAS_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'iris_hub_showtown': [
                'Iris_DL1_TAS_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'iris_hub_hidetown': [
                'Iris_DL1_TAS_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'iris_spawnpiston': [
                'Iris_DL1_TAS_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'iris_updatetheboard': [
                'Iris_DL1_TAS_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'start_boss_music': [
                'Iris_DL1_TAS_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'stop_boss_music': [
                'Iris_DL1_TAS_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'truckcleanup': [
                'Iris_DL1_TAS_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'truck_off': [
                'Iris_DL1_TAS_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'truck_on': [
                'Iris_DL1_TAS_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'debugpistoneject': [
                'Iris_DL1_TAS_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'debugtruckasaurus': [
                'Iris_DL1_TAS_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'debugvault': [
                'Iris_DL1_TAS_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
        },
        'iris_dl1_p': {
            'cop1_off': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'cop1_on': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'cop2_off': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'cop2_on': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'cop3_off': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'cop3_on': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'copr3_off': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'copr3_on': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'debuggassing': [
                'Iris_DL1_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'iris_arena_hidemaindoors': [
                'Iris_DL1_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'iris_arena_turnonpost': [
                'Iris_DL1_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'iris_closemaindoors': [
                'Iris_DL1_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'iris_dl1_battle1wave2on': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'iris_dl1_battle1wave3on': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'iris_dl1_battle1wave4on': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'iris_dl1_gasdoor': [
                'Iris_DL1_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'iris_dl1_wave1lights': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'iris_dl1_wave1lightstalk': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'iris_dl1_wave2lights': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'iris_dl1_wave3lights': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'iris_dl1_wave4lights': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'iris_hub_showtown': [
                'Iris_DL1_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'iris_hub_hidetown': [
                'Iris_DL1_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'iris_resetarenabattlenumbers': [
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
                'Iris_DL1_Battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'iris_updatetheboard': [
                'Iris_DL1_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'mission3teleportplayers': [
                'Iris_DL1_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'playerspawnedlowercheckpoint': [
                'Iris_DL1_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'start_arena_combat_music': [
                'Iris_DL1_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'stop_arena_combat_music': [
                'Iris_DL1_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
        },
        'stockade_p': {
            'opencomputerdoors': [
                'Stockade_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_6',
            ],
            'playmordecaiholo': [
                'Stockade_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_11',
            ],
            'stopholo': [
                'Stockade_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_12',
            ],
            'uncleteddy_attachblueprint': [
                'Stockade_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Uncle_Teddy.SeqEvent_RemoteEvent_0',
            ],
            'uncleteddy_machineshake': [
                'Stockade_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Uncle_Teddy.SeqEvent_RemoteEvent_1',
            ],
        },
        'fyrestone_p': {
            'alarm1': [
                'Fyrestone_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'carcheck': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_14',
            ],
            'change': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_15',
                'Fyrestone_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'djradiooff': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThisJustIn.SeqEvent_RemoteEvent_3',
            ],
            'djradioon': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThisJustIn.SeqEvent_RemoteEvent_2',
            ],
            'dontknowjack_turnonwindmill': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.YouDontKnowJack.Windmill.SeqEvent_RemoteEvent_1',
            ],
            'glowscale': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_13',
            ],
            'levelloaded': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_1',
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_10',
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_2',
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_3',
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_4',
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_9',
            ],
            'pipelastframe': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_8',
            ],
            'playmordecaiholo': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_11',
            ],
            'pumpstation2-1fx': [
                'Fyrestone_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_7',
            ],
            'pumpstation2-2fx': [
                'Fyrestone_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_5',
            ],
            'stopholo': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode15.SeqEvent_RemoteEvent_12',
            ],
            'thisjustin_radiostatioopened': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThisJustIn.SeqEvent_RemoteEvent_0',
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThisJustIn.SeqEvent_RemoteEvent_1',
            ],
            'youdontknowjack_turnonwindmillswitch': [
                'Fyrestone_Dynamic.TheWorld:PersistentLevel.Main_Sequence.YouDontKnowJack.Windmill.SeqEvent_RemoteEvent_0',
            ],
        },
        'iris_moxxi_p': {
        },
        'iris_hub_p': {
            'debugpiston': [
                'Iris_Hub_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'dustdevils': [
                'Iris_Hub_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'iris_arenaopenfirsttime': [
                'Iris_Hub_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'iris_dogwalkstart': [
                'Iris_Hub_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            'iris_hub_arenabattletravelaftertruck': [
                'Iris_Hub_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'iris_hub_arenabattletraveloff': [
                'Iris_Hub_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'iris_hub_arenabattletravelset': [
                'Iris_Hub_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'iris_hub_nuke1': [
                'Iris_Hub_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'iris_hub_nuke2': [
                'Iris_Hub_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'iris_hub_nuke3': [
                'Iris_Hub_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'iris_hub_releasedogai': [
                'Iris_Hub_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'iris_hub_resetdog': [
                'Iris_Hub_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'iris_hub_hidetown': [
                'Iris_Hub_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'iris_interviewcompleted': [
                'Iris_Hub_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'iris_updatetheboard': [
                'Iris_Hub_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'iris_walkthedog_dogdone': [
                'Iris_Hub_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'iris_walkthedog_iexist': [
                'Iris_Hub_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'manualsandstorm': [
                'Iris_Hub_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_startcrush_titlecard': [
                'Iris_Hub_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_startingrabposition': [
                'Iris_Hub_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'sandstorm': [
                'Iris_Hub_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'debugtina': [
                'Iris_Hub_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_titlecard_hidestuff': [
                'Iris_Hub_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
        },
        'iris_dl2_p': {
            'iris_dl2_openbar': [
                'Iris_DL2_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'iris_sullyaddoff': [
                'Iris_DL2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'iris_sullyaddon': [
                'Iris_DL2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'iris_sullyon': [
                'Iris_DL2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'iris_updatetheboard': [
                'Iris_DL2_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
        },
        'damtop_p': {
            'ere_callreinforcements': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_11',
            ],
            'ere_distancecheck': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_6',
            ],
            'ere_halfhealth': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_3',
            ],
            'ere_halfshields': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_2',
            ],
            'ere_shieldsdepleted': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_0',
            ],
            'ere_startmoonshot': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_5',
            ],
            'outofbody_spawnjett': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.M_OutOfBody.SeqEvent_RemoteEvent_0',
            ],
            're_destroypsychojumper': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Combat.script_psycho1.SeqEvent_RemoteEvent_7',
            ],
            're_ep6_damtopbattlecurrent': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Combat.SeqEvent_RemoteEvent_13',
            ],
            're_ep6_elementaldeath': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_9',
            ],
            're_ep6_gibdeath': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_8',
            ],
            're_ep6_regulardeath': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_7',
            ],
            're_halfhealth': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_1',
            ],
            're_jacklinedone': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_5',
            ],
            're_killfrigginconstuctor': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_8',
            ],
            're_startmoonshot': [
                'DamTop_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'rm_moonorbitlaunch': [
                'DamTop_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'rm_moonshotimpact': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Combat.Script_WoundedGuy.SeqEvent_RemoteEvent_5',
            ],
            're_banditscreamingatmoon': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Combat.Script_WoundedGuy.SeqEvent_RemoteEvent_0',
            ],
            're_prisonbotdies': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Dropship.script_DropShipController.SeqEvent_RemoteEvent_1',
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_12',
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_6',
            ],
            're_rolandpicksupgunfailsafe': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_0',
            ],
            'turnondistantbattlesound2': [
                'DamTop_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_bandithutloader1': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Combat.Script_BloodyEntrances.SeqEvent_RemoteEvent_13',
            ],
            're_destroybackhandloader': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Combat.MatineedPawnsMoments.script_TunnelBackhand.SeqEvent_RemoteEvent_0',
            ],
            're_distancecheck': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.Script_DistanceChecks.SeqEvent_RemoteEvent_1',
            ],
            're_endcatchpositionpark': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Dropship.script_DropShipController.SeqEvent_RemoteEvent_2',
            ],
            're_flyoverover': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Combat.IntroAiBattle.SeqEvent_RemoteEvent_2',
            ],
            're_goteleport': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_4',
            ],
            're_movetobarge': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_11',
            ],
            're_playcamfly': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Combat.IntroAiBattle.SeqEvent_RemoteEvent_1',
                'DamTop_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_0',
            ],
            're_rolandcallsoutbadass': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_9',
            ],
            're_rolandlanded': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_10',
            ],
            're_rolandrescued': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Dropship.script_DropShipController.SeqEvent_RemoteEvent_3',
            ],
            're_sendconstructor': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_3',
            ],
            're_sendfirstareabotstodoorarea': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.Combat.IntroAiBattle.SeqEvent_RemoteEvent_0',
            ],
            're_shieldsdepleted': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.ExternalRemoteEventManager.SeqEvent_RemoteEvent_4',
            ],
            're_turretkilled': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_2',
            ],
            're_wavecombatover': [
                'DamTop_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonBot.SeqEvent_RemoteEvent_7',
            ],
        },
        'dam_p': {
            'are_light02_off': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_9',
            ],
            'are_light02_on': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_10',
            ],
            'are_light03_off': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_0',
            ],
            'are_light03_on': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_1',
            ],
            'are_light04_off': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_4',
            ],
            'are_light04_on': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_3',
            ],
            'are_light05_off': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_5',
            ],
            'are_light05_on': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_6',
            ],
            'are_light_off': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_8',
            ],
            'are_light_on': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_7',
            ],
            'iamdan': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqEvent_RemoteEvent_4',
            ],
            'iamlee': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqEvent_RemoteEvent_5',
            ],
            'iammick': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqEvent_RemoteEvent_3',
            ],
            'iamralph': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqEvent_RemoteEvent_2',
            ],
            'outofbody_killloader': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Loader1340.SeqEvent_RemoteEvent_0',
            ],
            're_rolandcelldoorused': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_0',
            ],
            'spawnflinter': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.Happy_Easter.SeqEvent_RemoteEvent_2',
            ],
            'startwave2': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqEvent_RemoteEvent_6',
            ],
            'startwave3': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqEvent_RemoteEvent_8',
            ],
            'startwave4': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqEvent_RemoteEvent_7',
            ],
            'startwave5': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SplinterGroup.SeqEvent_RemoteEvent_0',
            ],
            'debugroland': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonIntroSequence.SeqEvent_RemoteEvent_2',
            ],
            're_rolandsnatch_hyperionbotambush': [
                'Dam_Combat.TheWorld:PersistentLevel.Main_Sequence.combatnearroland.SeqEvent_RemoteEvent_0',
            ],
            're_spawnprisonbot': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonIntroSequence.SeqEvent_RemoteEvent_0',
            ],
            're_startfleeingcombat': [
                'Dam_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.RolandPrisonIntroSequence.SeqEvent_RemoteEvent_1',
            ],
        },
        'boss_cliffs_p': {
            'bunkerdied': [
                'Boss_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Boss_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'bunker_autocannonkilled': [
                'Boss_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'disablepathblocking': [
                'Boss_Cliffs_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'lerpboss': [
                'Boss_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_ammohealthdrop': [
                'Boss_Cliffs_CombatLoader.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_autocannondeathforammo': [
                'Boss_Cliffs_CombatLoader.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_0',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_10',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_11',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_8',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_9',
            ],
            're_bunkercannondeath': [
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_1',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_2',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_4',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_5',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_6',
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LaserTraps.SeqEvent_RemoteEvent_7',
            ],
            're_hidefakebnk3rcollision': [
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BunkerTitleCard.SeqEvent_RemoteEvent_1',
            ],
            're_spawnbunkerplusplus': [
                'Boss_Cliffs_CombatLoader.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_startbunkerfight': [
                'Boss_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_startbunkertitlecard': [
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BunkerTitleCard.SeqEvent_RemoteEvent_3',
            ],
            'rm_bossmusicoff': [
                'Boss_Cliffs_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'rm_bossmusicon': [
                'Boss_Cliffs_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'rm_ep13_openjackdoor': [
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_0',
            ],
            'debugbunker': [
                'Boss_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BunkerTitleCard.SeqEvent_RemoteEvent_0',
            ],
        },
        'sage_cliffs_p': {
            'activatemurderers': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'chainlightning': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'firstwheelcorrect': [
                'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'firstwheelfalse': [
                'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'leashmurderers': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'm5_elite_savages_enable': [
                'SAGE_CLIFFS_COMBAT.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_claptrapsayscode': [
                'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'raid_activated': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'raid_checklockout': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'raid_lever_lockedout': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'raid_missioncomplete': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'resetmurderers': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'secondwheelcorrect': [
                'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'secondwheelfalse': [
                'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'spawnraidbosscheck': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'thirdwheelcorrect': [
                'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'thirdwheelfalse': [
                'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'unhideleveltransitioner': [
                'Sage_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'unleashmurderers': [
                'Sage_Cliffs_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
        },
        'caverns_p': {
            'crystalregenchallenge': [
                'Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SafeAndSound.SeqEvent_RemoteEvent_0',
            ],
            'minecart_startwheels': [
                'Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.SeqEvent_RemoteEvent_1',
            ],
            'minecart_stopwheels': [
                'Caverns_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MinecartMischief_0.SeqEvent_RemoteEvent_2',
            ],
            'oozebombtouched': [
                'caverns_p.TheWorld:PersistentLevel.Main_Sequence.LevelChallenges.SeqEvent_RemoteEvent_0',
            ],
        },
        'vogchamber_p': {
            'animplayer_teleporthands': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_44',
            ],
            'ep14_lilithteleportplayer': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'lilith_nameplateoff': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'lilith_nameplateon': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            're_activatefirstwaveteslatraps': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_6',
            ],
            're_activateplasmaexhaust': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PlasmaExhaust.SeqEvent_RemoteEvent_12',
            ],
            're_activatesecondwaveteslatraps': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_17',
            ],
            're_angelimage_fadein': [
                'VOGChamber_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_angelimage_fadeout': [
                'VOGChamber_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_angelintrocomplete': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_angelspawnammo': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_beginfirehawkphaseloop': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_2',
            ],
            're_chestspawndone': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Injector03.SeqEvent_RemoteEvent_28',
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Injector03.SeqEvent_RemoteEvent_41',
            ],
            're_chestspawnstart': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Injector03.SeqEvent_RemoteEvent_42',
            ],
            're_closeangeldoorintro': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqEvent_RemoteEvent_6',
            ],
            're_deactivateplasmaexhaust': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PlasmaExhaust.SeqEvent_RemoteEvent_11',
            ],
            're_dectivateteslatraps': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_0',
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_1',
            ],
            're_destroyallturrets': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            're_destroyangelshield': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.AngelShield.SeqEvent_RemoteEvent_0',
            ],
            're_ep13_panelhack01complete': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_ep13_panelhack02complete': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_ep13_panelhack03complete': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            're_ep14_hiderolandandlilith': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_etherealdissolve': [
                'VOGChamber_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_firehawk_enablephasewalk': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_12',
            ],
            're_firehawk_grabbingroland': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_firehawk_phaseblast': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_16',
            ],
            're_firehawk_phaseblastcomplete': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_18',
            ],
            're_firehawk_phaseblast_vo': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            're_firehawk_phasewalk': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_15',
            ],
            're_firehawk_readytophaseblast': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_25',
            ],
            're_firehawk_rolandatplat03': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_1',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_24',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_3',
            ],
            're_firehawk_teleportarrived': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            're_firstinjectorexpositioncomplete': [
                'VOGChamber_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_firstinjectorshot': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_hurtangel': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_initangelshield': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.AngelShield.SeqEvent_RemoteEvent_2',
            ],
            're_initializefirehawk': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_17',
            ],
            're_injector01exposed': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            're_injectordestroyed': [
                'VOGChamber_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_isplayerinlilithvolume': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_13',
            ],
            're_jt_angel_cantstopdefenses': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_52',
            ],
            're_jt_angel_dadihavetotell': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_8',
            ],
            're_jt_angel_destroyfirstinjector': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_60',
            ],
            're_jt_angel_destroytheothers': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_26',
            ],
            're_jt_angel_illhelpyou': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_53',
            ],
            're_jt_angel_injectorexposed': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_28',
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Roland_Reminder_Loop.SeqEvent_RemoteEvent_28',
            ],
            're_jt_angel_itsdone': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_12',
            ],
            're_jt_angel_jackendedmylife': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_59',
            ],
            're_jt_angel_lyingcoward': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_51',
            ],
            're_jt_angel_needyoutolower': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_55',
            ],
            're_jt_angel_nowroland': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_54',
            ],
            're_jt_angel_pain': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_25',
            ],
            're_jt_angel_promiseme': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_57',
            ],
            're_jt_angel_shutdownlightbridge': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_58',
            ],
            're_jt_angel_spawnammo': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_45',
            ],
            're_jt_angel_stoppingyou': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_4',
            ],
            're_jt_angel_thatshowheworks': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_56',
            ],
            're_jt_angel_trytoexposethem': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_27',
            ],
            're_jt_angel_youreanasshole': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_13',
            ],
            're_jt_jack_alrightbandit': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_15',
            ],
            're_jt_jack_angelangel': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_19',
            ],
            're_jt_jack_everythingivedone': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_50',
            ],
            're_jt_jack_hearingme': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_49',
            ],
            're_jt_jack_howbanditsfight': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_46',
            ],
            're_jt_jack_language': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_18',
            ],
            're_jt_jack_shieldsup': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_16',
            ],
            're_jt_jack_whatthehell': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_20',
            ],
            're_jt_jack_whocares': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_48',
            ],
            're_jt_jack_youcanstillstop': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_5',
            ],
            're_jt_jack_youreendangering': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_47',
            ],
            're_jumbotron_nobody': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_0',
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_9',
            ],
            're_jumbotron_off': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jumbotrons.SeqEvent_RemoteEvent_17',
            ],
            're_lastinjectordestroyed': [
                'VOGChamber_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_lightbridgeandlilith': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_lightbridgeoff': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LightBridges.SeqEvent_RemoteEvent_0',
            ],
            're_lightbridgeon': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LightBridges.SeqEvent_RemoteEvent_3',
            ],
            're_lilithintrovo': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_lilithteleportloop': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_19',
            ],
            're_lilith_praise_vo': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_openangeldoor': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqEvent_RemoteEvent_0',
            ],
            're_openangeldoorintro': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqEvent_RemoteEvent_7',
            ],
            're_panel03encounter_done': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_32',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_33',
            ],
            're_pauseammocrateloop': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            're_plasmaexhaustloop': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PlasmaExhaust.SeqEvent_RemoteEvent_0',
            ],
            're_raiseangelshield': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.AngelShield.SeqEvent_RemoteEvent_1',
            ],
            're_randomchatter_off': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_randomchatter_on': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
            ],
            're_rolandandlilithteleporttoangel': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_35',
            ],
            're_rolandisready': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_rolandleavepanel04': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_rolandopenpanel': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            're_roland_praise_vo': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_roland_turret_vo': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            're_setplayervars': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqEvent_RemoteEvent_3',
            ],
            're_shockpole01_up': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_3',
            ],
            're_shockpole02_up': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_4',
            ],
            're_shockpole03_up': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_7',
            ],
            're_shockpole04_up': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_10',
            ],
            're_shockpole05_up': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_11',
            ],
            're_shockpole06_up': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TeslaPoles.SeqEvent_RemoteEvent_5',
            ],
            're_spawnammochest': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            're_spawnammochest_vo': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            're_startammocrateloop': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            're_stopfirehawkloopforrolandteleport': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_0',
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_27',
            ],
            're_teleportfirehawkaway': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_10',
            ],
            're_teleportplayertoethereal': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqEvent_RemoteEvent_1',
            ],
            're_teleportplayers': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            're_teleportplayersfromethereal': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqEvent_RemoteEvent_2',
            ],
            're_teleportscreenfx': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqEvent_RemoteEvent_4',
            ],
            're_turnoffslagbeams': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_unpauseammocrateloop': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_vogchamberalarm': [
                'VOGChamber_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_vaultkeyspin': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_vaultkeyteleport': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'roland_flashlightoff': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'roland_flashlighton': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'roland_lowerthreat': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'roland_nameplateoff': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            'roland_nameplateon': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            'roland_raisethreat': [
                'VOGChamber_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'debugangeltitlecard': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EtherealEntry.SeqEvent_RemoteEvent_5',
            ],
            'debugrolanddeath': [
                'VOGChamber_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
        },
        'dark_forest_p': {
            'achieve_swordpullout': [
                'Dark_Forest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'destroyfoliage': [
                'Dark_Forest_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'destroyolpopdens': [
                'Dark_Forest_Combat.TheWorld:PersistentLevel.Main_Sequence.Plot_OverLeveledCombat.SeqEvent_RemoteEvent_0',
            ],
            'mre_cf_turnin': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_4',
            ],
            'mre_davlincallsout': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.PlotMission02.MeetUpWithDavlin.SeqEvent_RemoteEvent_0',
            ],
            'orclumbercamp_sapplanted': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_1',
            ],
            'postcrump_dropcage': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Crumpets.Cage_Crumpet.SeqEvent_RemoteEvent_0',
            ],
            'postcrump_vo4': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Crumpets.SeqEvent_RemoteEvent_4',
            ],
            're_cf_gunmortarin': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_2',
            ],
            're_cf_roll3': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_1',
            ],
            're_cf_startspinthree': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_6',
            ],
            're_esa_faketreecollision': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Ell_In_Shining_Armor.SeqEvent_RemoteEvent_2',
            ],
            're_esa_pickreal': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Ell_In_Shining_Armor.SeqEvent_RemoteEvent_0',
            ],
            're_esa_picksexy': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Ell_In_Shining_Armor.SeqEvent_RemoteEvent_1',
            ],
            're_sidepathdialogdone': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.Ell_In_Shining_Armor.SeqEvent_RemoteEvent_3',
            ],
            'treehugger_allhutsdestroyed': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_30',
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_4',
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_5',
            ],
            'treehugger_enablespawnhut1': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_3',
            ],
            'treehugger_enablespawnhut2': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_14',
            ],
            'treehugger_enablespawnhut3': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_15',
            ],
            'treehugger_enablespawnhut4': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_18',
            ],
            'treehugger_enablespawnhut5': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_19',
            ],
            'treehugger_enablespawnhut6': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_2',
            ],
            'treehugger_spawnhut1': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_10',
            ],
            'treehugger_spawnhut2': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_13',
            ],
            'treehugger_spawnhut3': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_16',
            ],
            'treehugger_spawnhut4': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_17',
            ],
            'treehugger_spawnhut5': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_20',
            ],
            'treehugger_spawnhut6': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_11',
            ],
            'treehugger_turninvo': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_6',
            ],
            'treehugger_turnoffcampcombat': [
                'Dark_Forest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'treehugger_turnoffmissiondens': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_29',
            ],
            'treehugger_turnoffperch1': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_31',
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_41',
            ],
            'treehugger_turnoffperch2': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_32',
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_40',
            ],
            'treehugger_turnoffperch3': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_33',
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_39',
            ],
            'treehugger_turnoffperch4': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_34',
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_38',
            ],
            'treehugger_turnoffperch5': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_35',
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_37',
            ],
            'treehugger_turnoffperch6': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_12',
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_36',
            ],
            'treehugger_turnoncampcombat': [
                'Dark_Forest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'treehugger_vo10': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_26',
            ],
            'treehugger_vo11': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_28',
            ],
            'treehugger_vo12': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_27',
            ],
            'treehugger_vo2': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_7',
            ],
            'treehugger_vo3': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_8',
            ],
            'treehugger_vo4': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_9',
            ],
            'treehugger_vo5': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_22',
            ],
            'treehugger_vo6': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_21',
            ],
            'treehugger_vo7': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_23',
            ],
            'treehugger_vo8': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_24',
            ],
            'treehugger_vo9': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.TreeHugger.SeqEvent_RemoteEvent_25',
            ],
            'check': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.PlotMission02.BloodFruitCollectionScripting.SeqEvent_RemoteEvent_1',
            ],
            're_bloodtreantspawned': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.PlotMission02.BloodFruitCollectionScripting.SeqEvent_RemoteEvent_2',
            ],
            're_change_tranquiltodark': [
                'Dark_Forest_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Dark_Forest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_enterforestchangemood': [
                'Dark_Forest_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Dark_Forest_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_set_dark': [
                'Dark_Forest_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'Dark_Forest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_set_lightback': [
                'Dark_Forest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_set_tranquil': [
                'Dark_Forest_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Dark_Forest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_dia_convoaboutqueen': [
                'Dark_Forest_Missions.TheWorld:PersistentLevel.Main_Sequence.PlotMission02.SeqEvent_RemoteEvent_3',
            ],
        },
        'castlekeep_p': {
            'achieve_swordpullout': [
                'CastleKeep_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'audio_play_teleport': [
                'CastleKeep_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'audio_sacrifice_explosion': [
                'CastleKeep_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'audio_storm_off': [
                'CastleKeep_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'audio_storm_on': [
                'CastleKeep_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'bigenemy': [
                'CastleKeep_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'disablescreenstorm': [
                'CastleKeep_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'enablealtar': [
                'CastleKeep_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_whoisontheelevator_bottom': [
                'CastleKeep_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_whoisontheelevator_top': [
                'CastleKeep_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'smallenemies': [
                'CastleKeep_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'start combat music': [
                'CastleKeep_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'stop_storm_audio': [
                'CastleKeep_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'toggleonelevatorspawns': [
                'CastleKeep_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'wheelused': [
                'CastleKeep_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_castlekeep_makerolandvisible': [
                'CastleKeep_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.CastleRoland.SeqEvent_RemoteEvent_1',
            ],
            're_creditfinished': [
                'CastleKeep_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.FeedButtstallion_LightBack.SeqEvent_RemoteEvent_1',
            ],
            're_energycharge': [
                'CastleKeep_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.FeedButtstallion_LightBack.SeqEvent_RemoteEvent_0',
            ],
            're_finaljackteleport': [
                'CastleKeep_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'CastleKeep_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.JackFight.SeqEvent_RemoteEvent_3',
            ],
            're_rolandspawned': [
                'CastleKeep_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.CastleRoland.SeqEvent_RemoteEvent_0',
                'CastleKeep_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.CastleRoland.SeqEvent_RemoteEvent_4',
            ],
            're_startcredits': [
                'CastleKeep_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.SeqEvent_RemoteEvent_0',
            ],
            're_teleporterused': [
                'CastleKeep_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.JackINI.SeqEvent_RemoteEvent_3',
            ],
            're_triggerbsfxchange': [
                'CastleKeep_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_triggerbslightchange': [
                'CastleKeep_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'CastleKeep_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_turnoffforjackfight': [
                'CastleKeep_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_turnoffskylightbstc': [
                'CastleKeep_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
        },
        'interlude_p': {
            'aggrocaravan': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.Cara-Van_Dialog.SeqEvent_RemoteEvent_9',
            ],
            'attack': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.Cara-Van_Dialog.SeqEvent_RemoteEvent_8',
            ],
            'caravandeath_off': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.SeqEvent_RemoteEvent_3',
            ],
            'caravandeath_on': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.SeqEvent_RemoteEvent_2',
            ],
            'caravanstart': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.SeqEvent_RemoteEvent_0',
            ],
            'crusherchallenge': [
                'Interlude_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'disablecaravan': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.SeqEvent_RemoteEvent_1',
            ],
            'disablecaravandialog': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.SeqEvent_RemoteEvent_4',
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.SeqEvent_RemoteEvent_7',
            ],
            'duelingbanjos_disablecars': [
                'Interlude_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'duelingbanjos_enablecars': [
                'Interlude_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'duelingbanjos_shothodunk': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DuelingBanjos.SeqEvent_RemoteEvent_0',
            ],
            'duelingbanjos_shotzaford': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DuelingBanjos.SeqEvent_RemoteEvent_1',
            ],
            'dustdevils': [
                'Interlude_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'ere_teleporttolift': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_06.SeqEvent_RemoteEvent_0',
            ],
            'enablecaravandialog': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.SeqEvent_RemoteEvent_5',
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.SeqEvent_RemoteEvent_8',
            ],
            'escortdeath': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cara-Van.SeqEvent_RemoteEvent_6',
            ],
            'goodbadmordecaiabortmove': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.GoodBadMordecai.SeqEvent_RemoteEvent_0',
            ],
            'pse_disablecars': [
                'Interlude_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'pse_enablecars': [
                'Interlude_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_startcrush_titlecard': [
                'Interlude_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_startingrabposition': [
                'Interlude_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'rm_anyvehicle_driverentered': [
                'Interlude_Combat.TheWorld:PersistentLevel.Main_Sequence.script_attackVehicle.SeqEvent_RemoteEvent_5',
            ],
            'rm_technicalvehicle_driverentered': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_06.SeqEvent_RemoteEvent_6',
            ],
            're_ellielookattechnical': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_06.SeqEvent_RemoteEvent_2',
            ],
            'riggedrace_spawnrace': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.1stPlace.SeqEvent_RemoteEvent_1',
            ],
            'sandstorm_audio_start': [
                'Interlude_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'sandstorm_audio_stop': [
                'Interlude_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'debugellie': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_06.SeqEvent_RemoteEvent_1',
            ],
            're_disablecarstation': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_06.SeqEvent_RemoteEvent_7',
            ],
            're_hidepreviewstuff': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_06.SeqEvent_RemoteEvent_8',
            ],
            're_sandstormoff': [
                'Interlude_Combat.TheWorld:PersistentLevel.Main_Sequence.script_attackVehicle.SeqEvent_RemoteEvent_1',
            ],
            're_sendellietostation': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_06.SeqEvent_RemoteEvent_5',
            ],
            're_uploadtemplateintocar': [
                'Interlude_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_06.SeqEvent_RemoteEvent_3',
            ],
        },
        'tundratrain_p': {
            'callloaders': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TrainStopAreaAndWilhelm.SeqEvent_RemoteEvent_7',
            ],
            'reveal_bots': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TrainStopAreaAndWilhelm.SeqEvent_RemoteEvent_2',
            ],
            'train1punched': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TrainStopAreaAndWilhelm.SeqEvent_RemoteEvent_3',
            ],
            'train3punched': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TrainStopAreaAndWilhelm.SeqEvent_RemoteEvent_5',
            ],
            'train4punched': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TrainStopAreaAndWilhelm.SeqEvent_RemoteEvent_6',
            ],
            'train5punched': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TrainStopAreaAndWilhelm.SeqEvent_RemoteEvent_4',
            ],
            'willhelmprobedead': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TrainStopAreaAndWilhelm.SeqEvent_RemoteEvent_1',
            ],
            're_firsttimethrough': [
                'TundraTrain_Combat.TheWorld:PersistentLevel.Main_Sequence.WilhelmLeadUpCombat.SeqEvent_RemoteEvent_0',
            ],
            're_punchagain': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TrainStopAreaAndWilhelm.SeqEvent_RemoteEvent_8',
            ],
            're_wilhelmspawned': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TrainStopAreaAndWilhelm.SeqEvent_RemoteEvent_0',
            ],
            're_shakesnow': [
                'TundraTrain_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.LeadUpToWilhelmEffects.SeqEvent_RemoteEvent_1',
            ],
        },
        'ash_p': {
            'arealboy_malattack': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.A_Real_Boy.SeqEvent_RemoteEvent_4',
            ],
            'arealboy_malisdead': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.A_Real_Boy.SeqEvent_RemoteEvent_1',
            ],
            'arealboy_turnoffmalspawner': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.A_Real_Boy.SeqEvent_RemoteEvent_3',
            ],
            'claptrapstarttyping': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqEvent_RemoteEvent_7',
            ],
            'claptrapstoptyping': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqEvent_RemoteEvent_6',
            ],
            'dk_barrelhit': [
                'Ash_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ep17_closeoutergates': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqEvent_RemoteEvent_3',
            ],
            'ep17_openoutergates': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqEvent_RemoteEvent_8',
            ],
            'ep17_claptrapgateseq1': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqEvent_RemoteEvent_2',
            ],
            'ep17_load_claptrapgateseq2': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqEvent_RemoteEvent_5',
            ],
            'ep17_load_claptrapgateseq3': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqEvent_RemoteEvent_1',
            ],
            'eruption': [
                'Ash_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'finalbotdock': [
                'Ash_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'killyourself_notready': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Kill_Yourself.SeqEvent_RemoteEvent_0',
            ],
            'killyourself_ready': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Kill_Yourself.SeqEvent_RemoteEvent_1',
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Kill_Yourself.SeqEvent_RemoteEvent_2',
            ],
            'kingmongslagged': [
                'Ash_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'lavafountainbridgecycle': [
                'Ash_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_levelchallengedishes': [
                'Ash_P.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_1',
            ],
            're_realboymalhold': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.A_Real_Boy.SeqEvent_RemoteEvent_0',
            ],
            're_realboymalrelease': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.A_Real_Boy.SeqEvent_RemoteEvent_2',
            ],
            're_turretssurvived': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode17.SeqEvent_RemoteEvent_0',
            ],
            'smagalsteelsthering': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Smagal.SeqEvent_RemoteEvent_4',
            ],
            'smagalvolcano': [
                'Ash_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'spawnbots': [
                'Ash_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'tiecut': [
                'Ash_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'volcanochallengeplay': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'volcanocycle': [
                'Ash_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'opendoors': [
                'Ash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Grandmother_House.SeqEvent_RemoteEvent_1',
            ],
            're_onmapstartevents': [
                'Ash_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
        },
        'banditslaughter_p': {
            'rm_conveyback': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'rm_conveyfrontleft': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'rm_conveyfrontright': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'rm_conveyleftsidehighest': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'rm_conveyleftsidelower': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'rm_conveyrightside': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'rm_doorsbottomfront': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'rm_doorsbottomright': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'rm_frontdoorleft': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'rm_frontdoorright': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'rm_sidedoor': [
                'BanditSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
        },
        'village_p': {
            'fakegeekguy_loopscrolls': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_0',
            ],
            'fakegeek_startrunner': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_4',
            ],
            'fakegeek_stopscroll2mat': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_1',
            ],
            'fakegeek_torguescroll2vo': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_6',
            ],
            'fakegeek_turninvo': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_2',
            ],
            'fakegeek_vo1': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_3',
            ],
            'fakegeek_vo2': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_5',
            ],
            'fakegeek_vo3': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_7',
            ],
            'fakegeek_vo4': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_8',
            ],
            'fakegeek_vo5': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_9',
            ],
            'fakegeek_vo6': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.FakeGeekGuy.SeqEvent_RemoteEvent_10',
            ],
            'mmo_turninvo': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.MMO.SeqEvent_RemoteEvent_13',
            ],
            'pathtoforestopenonload': [
                'Village_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'plot_turnonbarrel1': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.BlimpsExplode.SeqEvent_RemoteEvent_4',
            ],
            'plot_turnonbarrel2': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.BlimpsExplode.SeqEvent_RemoteEvent_3',
            ],
            'postcrump_turninvo': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Crumpets.SeqEvent_RemoteEvent_8',
            ],
            'postcrump_vo1': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Crumpets.SeqEvent_RemoteEvent_0',
            ],
            'postcrump_vo2': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Crumpets.SeqEvent_RemoteEvent_1',
            ],
            're_checkforplayersneargate': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.EllieAppearance.SeqEvent_RemoteEvent_0',
            ],
            're_esa_gobacktostart': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Ell_In_Shining_Armor.SeqEvent_RemoteEvent_1',
            ],
            're_esa_kickoffdialog': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Ell_In_Shining_Armor.SeqEvent_RemoteEvent_6',
            ],
            're_fb_dialogkickoff': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Feed_ButtStallion.SeqEvent_RemoteEvent_0',
            ],
            're_fb_turnin': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Feed_ButtStallion.SeqEvent_RemoteEvent_1',
            ],
            're_gotoscreen': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Ell_In_Shining_Armor.SeqEvent_RemoteEvent_0',
            ],
            're_ln_playturnin': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.LootNinja.SeqEvent_RemoteEvent_10',
            ],
            're_pb_dialogkickoff': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Pett_Buttstallion.SeqEvent_RemoteEvent_4',
            ],
            're_pb_turnin': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Pett_Buttstallion.SeqEvent_RemoteEvent_5',
            ],
            're_ri_completed': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Roll_Insight.SeqEvent_RemoteEvent_1',
            ],
            're_ri_startroll': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Roll_Insight.SeqEvent_RemoteEvent_0',
            ],
            're_wic_gobacktotown': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_11',
            ],
            're_wic_turnindialog': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_6',
            ],
            'sis_turninvo': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordStoner.SeqEvent_RemoteEvent_0',
            ],
            'sis_vo8': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordStoner.SeqEvent_RemoteEvent_1',
            ],
            'torguebamfedout': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.TorgueScripting.SeqEvent_RemoteEvent_4',
            ],
            'turnoffblimpset1': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.BlimpsExplode.BlimpWinches.SeqEvent_RemoteEvent_0',
            ],
            'turnoffblimpset2': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.BlimpsExplode.BlimpWinches.SeqEvent_RemoteEvent_2',
            ],
            're_blowupblimp1': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.BlimpsExplode.SeqEvent_RemoteEvent_2',
            ],
            're_blowupblimp2': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.BlimpsExplode.SeqEvent_RemoteEvent_1',
            ],
            're_blowupblimpsactive': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.BlimpsExplode.BlimpWinches.SeqEvent_RemoteEvent_1',
            ],
            're_davlinappeared': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.FirstGateGuardMoment.SeqEvent_RemoteEvent_3',
            ],
            're_doneapologizing': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.PunchGuysAndChase.SeqEvent_RemoteEvent_1',
            ],
            're_gateguardreappears': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.FirstGateGuardMoment.SeqEvent_RemoteEvent_0',
            ],
            're_jerk2punchedinface': [
                'Village_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Talktotownsfolk.SeqEvent_RemoteEvent_0',
            ],
            're_jerkpunchedinface': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.PunchGuysAndChase.SeqEvent_RemoteEvent_0',
            ],
            're_mission01activeonload': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.SeqEvent_RemoteEvent_1',
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.FirstGateGuardMoment.SeqEvent_RemoteEvent_1',
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.TorgueScripting.SeqEvent_RemoteEvent_2',
            ],
            're_movetopathing': [
                'Village_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Talktotownsfolk.SeqEvent_RemoteEvent_1',
            ],
            're_offall': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.BlimpsExplode.SeqEvent_RemoteEvent_0',
            ],
            're_onloadonly_blowupblimps-activecomplete': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.TorgueScripting.SeqEvent_RemoteEvent_6',
            ],
            're_senddavlintogate': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.FirstGateGuardMoment.SeqEvent_RemoteEvent_2',
            ],
            're_sendtorgueonperchpath': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.TorgueScripting.SeqEvent_RemoteEvent_5',
            ],
            're_torgueinstocks': [
                'Village_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.TorgueScripting.SeqEvent_RemoteEvent_1',
            ],
            're_turnontransition': [
                'Village_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
        },
        'iris_dl3_p': {
            'blimpcounterattack': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_98',
            ],
            'blimpfirelcannonlower': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_69',
            ],
            'blimpfirelcannonupper': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_67',
            ],
            'blimpfirelwingturret': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            'blimpfirercannonlower': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_70',
            ],
            'blimpfirercannonupper': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_68',
            ],
            'blimpfirerwingturret': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'blimphpatfiftypercent': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_86',
            ],
            'blimphpatseventypercent': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
            ],
            'blimphpatthirtypercent': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'blimphpatzeropercent': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_76',
            ],
            'blimpintrodone': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'blimppath12to3close': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_57',
            ],
            'blimppath12to3far': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_78',
            ],
            'blimppath12to6across': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_52',
            ],
            'blimppath12to9close': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_82',
            ],
            'blimppath12to9far': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_62',
            ],
            'blimppath3to12close': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_81',
            ],
            'blimppath3to12far': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_61',
            ],
            'blimppath3to6close': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_56',
            ],
            'blimppath3to6far': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_79',
            ],
            'blimppath3to9across': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'blimppath6to12across': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            'blimppath6to3close': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_80',
            ],
            'blimppath6to3far': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_60',
            ],
            'blimppath6to9close': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_59',
            ],
            'blimppath6to9far': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_75',
            ],
            'blimppath9to12close': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_58',
            ],
            'blimppath9to12far': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_77',
            ],
            'blimppath9to3across': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_53',
            ],
            'blimppath9to6close': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_83',
            ],
            'blimppath9to6far': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'blimpshieldatfiftypercent': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            'blimpshieldatzeropercent': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_85',
            ],
            'cargogyro01destroyed': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_107',
            ],
            'cargogyro01gotodone': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_100',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_101',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_103',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_171',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_182',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_183',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_184',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_185',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_186',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_187',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_91',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_92',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_95',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_97',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_99',
            ],
            'cargogyro01gotostart': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_108',
            ],
            'cargogyro01spawned': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_93',
            ],
            'cargogyro02destroyed': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_124',
            ],
            'cargogyro02gotodone': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_112',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_113',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_114',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_115',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_116',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_117',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_118',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_119',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_121',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_122',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_123',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'cargogyro02gotostart': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_109',
            ],
            'cargogyro02spawned': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_120',
            ],
            'cargogyro03destroyed': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_139',
            ],
            'cargogyro03gotodone': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_140',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_141',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_142',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_144',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_145',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_146',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_147',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_148',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_149',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_150',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_151',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_152',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_153',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_188',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_189',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_190',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_191',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_192',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_193',
            ],
            'cargogyro03gotostart': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_111',
            ],
            'cargogyro03spawned': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_143',
            ],
            'cargogyro04destroyed': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_167',
            ],
            'cargogyro04gotodone': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_154',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_155',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_156',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_157',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_158',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_159',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_160',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_161',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_162',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_164',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_165',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_166',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_168',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_169',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_170',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'cargogyro04gotostart': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_110',
            ],
            'cargogyro04spawned': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_163',
            ],
            'cargogyro05destroyed': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_51',
            ],
            'cargogyro05gotodone': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_102',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_126',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_127',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_128',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_129',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_130',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_131',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_132',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_133',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_134',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_135',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_176',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_177',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_178',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_179',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_180',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_181',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_54',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_90',
            ],
            'cargogyro05gotostart': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'cargogyro05spawned': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_125',
            ],
            'cargogyro06destroyed': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_106',
            ],
            'cargogyro06gotodone': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_104',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_105',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_136',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_137',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_138',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_50',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_55',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_63',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_64',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_65',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_66',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_87',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_88',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_89',
            ],
            'cargogyro06gotostart': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'cargogyro06spawned': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'cargogyrotier01starting': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_172',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_173',
            ],
            'cargogyrotier02starting': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_174',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_96',
            ],
            'cargogyrotier03starting': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_94',
            ],
            'carpetbomb': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            'debugflyboy': [
                'Iris_DL3_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'ep5battle_gyroscomplete': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_175',
            ],
            'ep5battle_gyroscomplete2': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_194',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'ep5battle_gyroscomplete3': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_195',
            ],
            'forcelcannonsfire': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            'forcercannonsfire': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            'iris_dl3_husbandskagoff': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            'iris_dl3_opendoor01': [
                'Iris_DL3_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'iris_dl3_opendoor02': [
                'Iris_DL3_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'iris_dl3_prephusbandskagden': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
            ],
            'iris_dl3_uriahoff': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_44',
            ],
            'iris_dl3_uriahon': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_73',
            ],
            'iris_forgespeekerflyboydead': [
                'Iris_DL3_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'iris_gyrobattle_playerspawned': [
                'Iris_DL3_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'iris_knockingonheavendoorend': [
                'Iris_DL3_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'iris_m_commappeal_resetdens': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_196',
            ],
            'lcannonlowerfinished': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_45',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_71',
            ],
            'lcannonupperfinished': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_47',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_48',
            ],
            'playerusingturret': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_74',
            ],
            'rcannonlowerfinished': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_49',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_72',
            ],
            'rcannonupperfinished': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
            ],
            'rm_moonorbitlaunch': [
                'Iris_DL3_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'requestlcannonsfire': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'requestrcannonsfire': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'restorestance': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_84',
            ],
            'setbattle_gyrofight': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'setbattle_gyrofight2': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'setbattle_gyrofight3': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'startcannoncooldowntimer': [
                'Iris_DL3_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'start_blimp_boss_music': [
                'Iris_DL3_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'stop_blimp+boss_music': [
                'Iris_DL3_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
        },
        'fridge_p': {
            're_crankspawn1': [
                'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_crankspawn2': [
                'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_crankspawn3': [
                'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_crankspawn4': [
                'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_dragondoorcombat': [
                'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_0',
            ],
            're_foundfrozenrat': [
                'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.LevelChallenges.SeqEvent_RemoteEvent_2',
            ],
            're_resblocker': [
                'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_2',
            ],
            're_stopdragondoorcombat': [
                'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_stopsewercombat': [
                'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_togglesewercombat': [
                'Fridge_P.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_1',
            ],
            're_togglesewercombatbadass': [
                'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_turnoffbigboyroom': [
                'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_turnonbigboyroom': [
                'Fridge_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_wakebigboy': [
                'Fridge_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Fridge_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NoteToSelf.SeqEvent_RemoteEvent_0',
            ],
        },
        'hypinterlude_p': {
            'ere_halfhealth': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_5',
            ],
            'ere_halfshields': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_8',
            ],
            'ere_shieldsdepleted': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_3',
            ],
            'nightend': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'nightstart': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'pickedupgun': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_12',
            ],
            're_prisonbotdies': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_1',
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_6',
            ],
            're_rolandpicksupgunfailsafe': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_0',
            ],
            'sandstorm_audio_start': [
                'HypInterlude_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'sandstorm_audio_stop': [
                'HypInterlude_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_closeall': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_15',
            ],
            're_followupcombatover': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_19',
            ],
            're_goteleport': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_4',
            ],
            're_localdendepleted': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_20',
            ],
            're_rolandlanded': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_23',
            ],
            're_throwturretone': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_17',
            ],
            're_turretkilled': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_2',
            ],
            're_reinforcements': [
                'HypInterlude_P.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_16',
            ],
        },
        'icecanyon_p': {
            'animplayer_teleporthands': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'ep5_lilithphaseblastgibbandits': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'ep5_lilith_downstate': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'ep5_lilith_finalphaseblast': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'ep5_lilith_giveeridium': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'ep5_lilith_inittouch': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'ep5_lilith_inittouch2': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'ep5_lilith_needseridium': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ep5_lilith_phaseblast': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'ep5_lilith_playerrevived': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'ep5_lilith_puthanddown': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'ep5_lilith_titlecard': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'ep5_lilith_waiting': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'ep6_lilithteleportplayer': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'lightmatch_spawnmatchstick': [
                'IceCanyon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ChildrenOfFirehawk_SideMission.SeqEvent_RemoteEvent_1',
            ],
            'monstermash3_jumpdown': [
                'IceCanyon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MonsterMash3.SeqEvent_RemoteEvent_0',
            ],
            're_ep5_activatebloodshotattackers': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_ep5_angeltrapwarningcomplete': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_ep5_beginattackwave0': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_ep5_flamingchump': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_ep5_lilithbattle_playerkill': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_6',
            ],
            're_ep5_removeexitblocker': [
                'IceCanyon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode05.SeqEvent_RemoteEvent_2',
            ],
            're_firehawk_enablephasewalk': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_12',
            ],
            're_firehawk_firstappearance': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_17',
            ],
            're_firehawk_firstphasewalk': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_9',
            ],
            're_firehawk_midpointbreak': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_14',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_28',
            ],
            're_firehawk_midpointbreakover': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_firehawk_notreadytophaseblast': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_20',
            ],
            're_firehawk_phaseblast': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_16',
            ],
            're_firehawk_phaseblastcomplete': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_1',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_18',
            ],
            're_firehawk_phaseblast_vo': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_30',
            ],
            're_firehawk_phasewalk': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_15',
            ],
            're_firehawk_readytophaseblast': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_21',
            ],
            're_firehawk_wave00loop': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_2',
            ],
            're_firstwarriorearthquake': [
                'IceCanyon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode05.SeqEvent_RemoteEvent_0',
            ],
            're_isplayerinlilithvolume': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_13',
            ],
            're_lilithnameplateoff': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_25',
            ],
            're_lilithnameplateon': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_26',
            ],
            're_lilithreturntocenter': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_lilithteleportloop': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_19',
            ],
            're_randomchatter_off': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_23',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_34',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_4',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_5',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_7',
            ],
            're_randomchatter_on': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_0',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_11',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_22',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_39',
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_8',
            ],
            're_teleportfirehawkaway': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.Lilith.SeqEvent_RemoteEvent_10',
            ],
            're_warriorearthquake': [
                'IceCanyon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode05.SeqEvent_RemoteEvent_11',
            ],
            'debuglilith': [
                'IceCanyon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
        },
        'hunger_p': {
            'boss_music_off': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'boss_music_on': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'debug_foodout': [
                'Hunger_Machinery.TheWorld:PersistentLevel.Main_Sequence.TakeFoodOut.SeqEvent_RemoteEvent_0',
            ],
            'defaultevent': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_4',
            ],
            'end_bakerthoughtlocked': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_0',
            ],
            'loots': [
                'Hunger_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'music_stinger': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_activatebigintroelevatorcontrols': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_almostdone': [
                'Hunger_Machinery.TheWorld:PersistentLevel.Main_Sequence.GrindTheMeat.SeqEvent_RemoteEvent_1',
            ],
            're_blowup': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.GameshowInterview.SeqEvent_RemoteEvent_20',
            ],
            're_cameradestroyed': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.TorgueLockpickDoor.SeqEvent_RemoteEvent_1',
            ],
            're_disableelevatorvolumetesting': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_elevator1_quicktrip': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_elevator2_quicktrip': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_elevator3_quicktrip': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_elevator4_quicktrip': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_enableelevatorvolumetesting': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_foundcandy': [
                'Hunger_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_grandma1fail': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_28',
            ],
            're_grandma2fail': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_1',
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_23',
            ],
            're_grandmastory1turnin': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_32',
            ],
            're_grandmastory2turnin': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_27',
            ],
            're_interview': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.GameshowInterview.SeqEvent_RemoteEvent_22',
            ],
            're_prestory2check': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_30',
            ],
            're_removefakeelevatorwaypoint': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_rightchefdoor': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_8',
            ],
            're_runnableclosearenadoor': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_0',
            ],
            're_runnableopenarenadoor': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_1',
            ],
            're_someonetuggedcombatmeat': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_10',
            ],
            're_someonetuggedpuzzlemeat': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_11',
            ],
            're_startbigelevatorintro': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_startbigelevatorintrorunnable': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.RunnableBoss.SeqEvent_RemoteEvent_9',
            ],
            're_startbigturkeyintrorunnable': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.RunnableBoss.SeqEvent_RemoteEvent_11',
            ],
            're_startchefcombatload': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.KillTheChefs.SeqEvent_RemoteEvent_2',
            ],
            're_startgrandmastory1': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_29',
            ],
            're_startgrandmastory2': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_24',
            ],
            're_statesaver_music_off': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_statesaver_music_on': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_stopgrandmastory2check': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_31',
            ],
            're_stopprestorycheck': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_0',
            ],
            're_topchefdoor': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_32',
            ],
            're_torguesidekickoff': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SideMissionDialog.SeqEvent_RemoteEvent_19',
            ],
            're_turkeyisvulnerable': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_leftchefdoor': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_9',
            ],
            're_togglefreezerdoordialog': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Doors.TorgueLockpickDoor.SeqEvent_RemoteEvent_9',
            ],
            'sfx_oven_off': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'sfx_oven_on': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'sfx_crowd_cheer_playerwin': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'start_bakerthoughtlocked': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_1',
            ],
            'stopflames': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Conveyor.SeqEvent_RemoteEvent_0',
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Conveyor.SeqEvent_RemoteEvent_1',
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Conveyor.SeqEvent_RemoteEvent_2',
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Conveyor.SeqEvent_RemoteEvent_3',
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Conveyor.SeqEvent_RemoteEvent_4',
            ],
            'troyfreezer': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.FirstTributeFight.SeqEvent_RemoteEvent_1',
            ],
            'troy_jetpacker': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SecondTributeFight.SeqEvent_RemoteEvent_0',
            ],
            'world_music_on': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'world_music_off': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'asdf': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_23',
            ],
            're_defendfood_buttonmidgetwave': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_29',
            ],
            're_defendfood_incineratortrib': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_22',
            ],
            're_defendfood_lynchwoodtrib': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_21',
            ],
            're_defendfood_tributepause1': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_15',
            ],
            're_defendfood_wave1': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_12',
            ],
            're_defendfood_wave2': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_13',
            ],
            're_defendfood_wave3': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_14',
            ],
            're_dialogpostlockpick': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_0',
            ],
            're_dialog_playintrodialog': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_3',
            ],
            're_dialog_turkeyintrodialogdone': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_dialog_walkntalkdialogdone': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.TorgueWalkNTalk.SeqEvent_RemoteEvent_2',
            ],
            're_door_elevatorroom': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_14',
            ],
            're_door_elevatorroom_onload': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_15',
            ],
            're_door_outside_onload': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_9',
            ],
            're_door_torgue': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_1',
            ],
            're_lastmeattugged': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.FirstTributeFight.SeqEvent_RemoteEvent_0',
            ],
            're_liftfoodintoposition': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_makechefsaggro': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.KillTheChefs.SeqEvent_RemoteEvent_0',
            ],
            're_opencurtaindoor': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_0',
            ],
            're_opengrinddialog': [
                'Hunger_Machinery.TheWorld:PersistentLevel.Main_Sequence.GrindTheMeat.SeqEvent_RemoteEvent_3',
                'Hunger_Machinery.TheWorld:PersistentLevel.Main_Sequence.GrindTheMeat.ReleaseMeat.SeqEvent_RemoteEvent_3',
            ],
            're_oventurnedoff': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_3',
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_8',
            ],
            're_pausegrinddialog': [
                'Hunger_Machinery.TheWorld:PersistentLevel.Main_Sequence.GrindTheMeat.SeqEvent_RemoteEvent_2',
                'Hunger_Machinery.TheWorld:PersistentLevel.Main_Sequence.GrindTheMeat.ReleaseMeat.SeqEvent_RemoteEvent_2',
            ],
            're_playaddintrodialog': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.GameshowInterview.SeqEvent_RemoteEvent_7',
            ],
            're_playerhitsgrinderone': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Hunger_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_playerhitsgrindertwo': [
                'HUNGER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'Hunger_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_releasebigbird': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_reversefoodpiston': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_reverseshields': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SpawnTributes.SeqEvent_RemoteEvent_18',
            ],
            're_risemeatoutofreach': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.GrabMeat.SeqEvent_RemoteEvent_8',
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_8',
            ],
            're_risemeatoutofreach_reverse': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.GrabMeat.SeqEvent_RemoteEvent_2',
            ],
            're_sendcamsaway': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.IntroCams.SeqEvent_RemoteEvent_1',
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.IntroCams.SeqEvent_RemoteEvent_5',
            ],
            're_setsigntoblack': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.GameshowInterview.ApplauseSign.SeqEvent_RemoteEvent_0',
            ],
            're_spawnencounter': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_16',
            ],
            're_spawntributes': [
                'Hunger_Boss.TheWorld:PersistentLevel.Main_Sequence.SpawnTributes.SeqEvent_RemoteEvent_19',
            ],
            're_startconveyor': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.Matinees.SeqEvent_RemoteEvent_0',
            ],
            're_startplayerchecks': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_10',
            ],
            're_stopplayerchecks': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_27',
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_30',
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_9',
            ],
            're_torguetalkedto': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.TorgueWalkNTalk.SeqEvent_RemoteEvent_4',
            ],
            're_turncamboton': [
                'Hunger_Dynamic.TheWorld:PersistentLevel.Main_Sequence.CamBot.SeqEvent_RemoteEvent_8',
            ],
            're_turnoffall': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.StabberJabber.SeqEvent_RemoteEvent_4',
            ],
            're_turnoffreminderglowy': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_2',
            ],
            're_turnonfriendlychefs': [
                'Hunger_Mission_1.TheWorld:PersistentLevel.Main_Sequence.KillTheChefs.SeqEvent_RemoteEvent_1',
            ],
            're_turnongameshowcameras': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_2',
            ],
            're_turnonintroblocker': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.GameshowInterview.SeqEvent_RemoteEvent_4',
            ],
            're_turnonreminderglowy': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_1',
            ],
            're_updatewakejabber': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.StabberJabber.SeqEvent_RemoteEvent_1',
            ],
            're_buttondefended': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_32',
            ],
            're_buttonnotdefended': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_33',
            ],
            're_dia_afterslagging': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_0',
            ],
            're_dia_approachstabbers': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_15',
            ],
            're_dia_cookingdone': [
                'Hunger_Machinery.TheWorld:PersistentLevel.Main_Sequence.PoisonMeal.SeqEvent_RemoteEvent_6',
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_6',
            ],
            're_dia_finalglandpickup': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_24',
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.StabberJabber.SeqEvent_RemoteEvent_24',
            ],
            're_dia_getslagweapon': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_21',
            ],
            're_dia_glandpickup': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_22',
            ],
            're_dia_initialovenstart': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_2',
            ],
            're_dia_noslagstabberdeath': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_11',
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_19',
            ],
            're_dia_ovenfiller': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_18',
            ],
            're_dia_oventurnedoff': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_5',
            ],
            're_dia_poisonmeal': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_16',
            ],
            're_dia_slagjacker': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_18',
            ],
            're_dia_startoven': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_1',
            ],
            're_dia_wakeupstabbers': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_17',
            ],
            're_dia_walkingfromstabbers': [
                'Hunger_Mission_2.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_26',
            ],
            're_dialogoveroven': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_35',
            ],
            're_grandmacry': [
                'Hunger_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_ovenbuttonpressed': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_6',
            ],
            're_spawnintrocams': [
                'Hunger_Mission_Intro.TheWorld:PersistentLevel.Main_Sequence.IntroCams.SeqEvent_RemoteEvent_3',
            ],
            're_turnoffencounters': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_20',
            ],
            'spawnbuttonmidget': [
                'Hunger_Mission_3.TheWorld:PersistentLevel.Main_Sequence.DefendTheCook.SeqEvent_RemoteEvent_28',
            ],
        },
        'sage_hyperionship_p': {
            'bossmusic_off': [
                'Sage_HyperionShip_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'bossmusic_on': [
                'Sage_HyperionShip_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'stage1bstart': [
                'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'stage1dstart': [
                'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'stage2start': [
                'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'turnoffblockers_01': [
                'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'turnoffblockers_02': [
                'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'turnoffblockers_03': [
                'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'debugboss': [
                'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'debugnaka': [
                'Sage_HyperionShip_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
        },
        'pumpkin_patch_p': {
            'addchancedropbone1': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SkeletonKey.SeqEvent_RemoteEvent_12',
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SkeletonKey.SeqEvent_RemoteEvent_4',
            ],
            'addchancedropbone2': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SkeletonKey.SeqEvent_RemoteEvent_13',
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SkeletonKey.SeqEvent_RemoteEvent_5',
            ],
            'addchancedropbone3': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SkeletonKey.SeqEvent_RemoteEvent_14',
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SkeletonKey.SeqEvent_RemoteEvent_6',
            ],
            'allowbloodvalvetobeusedagain': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodField.SeqEvent_RemoteEvent_6',
            ],
            'bloodharvest_desecrategarden': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodField.SeqEvent_RemoteEvent_0',
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodField.SeqEvent_RemoteEvent_12',
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodField.SeqEvent_RemoteEvent_7',
            ],
            'bloodharvest_dialog2': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'bloodharvest_dialog4': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'bloodharvest_dialog5': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'bloodharvest_forgehammermat': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Blacksmith.SeqEvent_RemoteEvent_0',
            ],
            'bloodharvest_opengate': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gate.SeqEvent_RemoteEvent_0',
            ],
            'bloodharvest_spawnsully': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Blacksmith.SeqEvent_RemoteEvent_3',
            ],
            'bossbarswitch': [
                'Pumpkin_Patch_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'deathgoreon': [
                'Pumpkin_Patch_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'disableelevator': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'enableelevator': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'enchantedskeletonspawned': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'forcegate': [
                'PUMPKIN_PATCH_COMBAT.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_completecauldron': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClarkCombat.SeqEvent_RemoteEvent_0',
            ],
            're_completechurchfires': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClarkCombat.SeqEvent_RemoteEvent_2',
            ],
            're_completekingpin': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClarkCombat.SeqEvent_RemoteEvent_1',
            ],
            're_completetvs': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClarkCombat.SeqEvent_RemoteEvent_3',
            ],
            're_disablecombat': [
                'PUMPKIN_PATCH_COMBAT.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_drainfield': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodField.SeqEvent_RemoteEvent_1',
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodField.SeqEvent_RemoteEvent_8',
            ],
            're_enablecombat': [
                'PUMPKIN_PATCH_COMBAT.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_openforgeexit': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Blacksmith.SeqEvent_RemoteEvent_9',
            ],
            're_statesaver_door_open': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ChurchFires.SeqEvent_RemoteEvent_4',
            ],
            're_timefortktotalkaboutclosedgate': [
                'Pumpkin_Patch_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gate.SeqEvent_RemoteEvent_1',
            ],
            'spawnmissionpumpkinking': [
                'Pumpkin_Patch_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Pumpkin_Patch_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'start boss music': [
                'PUMPKIN_PATCH_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'stop boss music': [
                'PUMPKIN_PATCH_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'testcombat': [
                'PUMPKIN_PATCH_COMBAT.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
        },
        'castleexterior_p': {
            'achieve_swordpullout': [
                'CastleExterior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'destroy weather system': [
                'CastleExterior_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_attackthedarknesswithmagicmissile': [
                'CastleExterior_P.TheWorld:PersistentLevel.Main_Sequence.Environment.SeqEvent_RemoteEvent_1',
            ],
            're_headtomimicarea': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_6',
            ],
            're_ln_callout': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_2',
            ],
            're_ln_guykilled': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_1',
            ],
            're_ln_guykilled2': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_4',
            ],
            're_ln_guykilled3': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_3',
            ],
            're_ln_kickoff': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_0',
            ],
            're_ln_playtorgueline': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_5',
            ],
            're_ln_searchboilload': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_9',
            ],
            're_ln_stupidsaveloadbug': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_10',
            ],
            're_playerentereddownstate': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.SeqEvent_RemoteEvent_7',
            ],
            're_returntopatrol': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_8',
            ],
            're_staystillgoober': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Loot_Ninja.SeqEvent_RemoteEvent_7',
            ],
            're_wic_blockdoors': [
                'CastleExterior_P.TheWorld:PersistentLevel.Main_Sequence.Environment.SeqEvent_RemoteEvent_0',
            ],
            're_wic_cower': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_5',
            ],
            're_wic_enabledoor': [
                'CastleExterior_P.TheWorld:PersistentLevel.Main_Sequence.Environment.SeqEvent_RemoteEvent_2',
            ],
            're_wic_foundjeffery': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_2',
            ],
            're_wic_guardskilled': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_4',
            ],
            're_wic_moveforward': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_3',
            ],
            're_wic_slap1': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_9',
            ],
            're_wic_slap2': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_10',
            ],
            're_wic_slap3': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_8',
            ],
            're_wic_set0': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_12',
            ],
            're_wic_set1': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_11',
            ],
            're_wic_set2': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_6',
            ],
            're_wic_startdefeateddialog': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_7',
            ],
            'startfightingroland': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.SeqEvent_RemoteEvent_1',
            ],
            'wic_disablebossbar': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_0',
            ],
            'wic_togglebossbar': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Winter_Is_Coming.SeqEvent_RemoteEvent_1',
            ],
            're_destroyturnoffpart': [
                'CastleExterior_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_rolandvisible': [
                'CastleExterior_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission04.SeqEvent_RemoteEvent_6',
            ],
        },
        'orchid_caves_p': {
            'raid3_activated': [
                'Orchid_Caves_Raid_C.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'raid3_checklockout': [
                'Orchid_Caves_Raid_C.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'raid3_missioncomplete': [
                'Orchid_Caves_Raid_C.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'reapercheck': [
                'Orchid_Caves_Raid_C.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'start raid music': [
                'Orchid_Caves_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'stop raid music': [
                'Orchid_Caves_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'debugsandman': [
                'Orchid_Caves_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
        },
        'finalbossascent_p': {
            'brickspawned': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_18',
            ],
            'conditional_disableforcefield': [
                'FinalBossAscent_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'cuemoonshot': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_10',
            ],
            'destroybridge': [
                'FinalBossAscent_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'disablearmaudio_1': [
                'FinalBossAscent_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'disablearmaudio_2': [
                'FinalBossAscent_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'disablearmaudio_3': [
                'FinalBossAscent_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'disablebridge': [
                'FinalBossAscent_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'distanceorbital': [
                'FinalBossAscent_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'dropship1idle': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_11',
            ],
            'dropship1_idlestop': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_3',
            ],
            'enablerepairprobes': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'firefortressprojectile': [
                'FinalBossAscent_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'firemoonshot': [
                'FinalBossAscent_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'fireoutpostprojectile': [
                'FinalBossAscent_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'forcefield': [
                'FinalBossAscent_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'fortresspatrols': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.FortressCombat.SeqEvent_RemoteEvent_13',
            ],
            'fortresswave2complete': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_12',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_14',
            ],
            'fortresswave3complete': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_13',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_21',
            ],
            'longwaller1_stop': [
                'FinalBossAscent_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LongWaller_1.SeqEvent_RemoteEvent_1',
            ],
            'longwaller2_stop': [
                'FinalBossAscent_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LongWaller_2.SeqEvent_RemoteEvent_0',
            ],
            'longwaller3_stop': [
                'FinalBossAscent_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LongWaller_3.SeqEvent_RemoteEvent_0',
            ],
            'mordinposition': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_1',
            ],
            'mordinsnipingposition': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_8',
            ],
            'mordspawned': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_17',
            ],
            'mordecai_leaveoutpost': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_16',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_5',
            ],
            'movemordecai': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_15',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_4',
            ],
            're_ep17_ascentcomplete_load': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_2',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_20',
                'FinalBossAscent_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_ep17_brickkilldialog': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_39',
            ],
            're_ep17_disablebrickchatter': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_34',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_37',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_42',
            ],
            're_ep17_enablebrickchatter': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_35',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_38',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_41',
            ],
            're_ep17_playerdead': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_36',
            ],
            're_ep17_playerdown': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_40',
            ],
            'sendbricktoscriptedspot': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_0',
            ],
            'sendjetstobarge': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_19',
            ],
            'sendjetstobarge2': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_9',
            ],
            'spawnjetloaders': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_6',
            ],
            'spawn_back_l': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.Spawn_Back_L.SeqEvent_RemoteEvent_4',
            ],
            'spawn_back_r': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.Spawn_Back_R.SeqEvent_RemoteEvent_1',
            ],
            'spawn_dropshipjetrelease': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.Dropship_JETSpawn_0.SeqEvent_RemoteEvent_3',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.Dropship_JETSpawn_1.SeqEvent_RemoteEvent_2',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.Dropship_JETSpawn_2.SeqEvent_RemoteEvent_2',
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.Dropship_JETSpawn_3.SeqEvent_RemoteEvent_1',
            ],
            'spawn_front_l': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.Spawn_Front_L.SeqEvent_RemoteEvent_5',
            ],
            'spawn_front_r': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.Spawn_Front_R.SeqEvent_RemoteEvent_0',
            ],
            'turretsoff': [
                'FinalBossAscent_Combat.TheWorld:PersistentLevel.Main_Sequence.CrimsonBarge.SeqEvent_RemoteEvent_7',
            ],
        },
        'outwash_p': {
            'beacon_damaged_siren': [
                'Outwash_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'beacon_damaged_siren_stop': [
                'Outwash_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ere_startmoonshot_1': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.thresherIntro.SeqEvent_RemoteEvent_1',
            ],
            'marcus_radio_music_off': [
                'Outwash_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'marcus_radio_music_on': [
                'Outwash_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'mothersday_henry50': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MothersDayGift.SeqEvent_RemoteEvent_0',
            ],
            'none': [
                'Outwash_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'overlooked_guardtakedamage': [
                'Outwash_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_0',
                'Outwash_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_3',
                'Outwash_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_5',
            ],
            'overlooked_ropatrol': [
                'Outwash_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_7',
            ],
            'overlooked_spawnvendingguards': [
                'Outwash_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_6',
            ],
            'overlooked_targetacquired': [
                'Outwash_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_1',
                'Outwash_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_4',
            ],
            'playgrinder': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked2.SeqEvent_RemoteEvent_0',
            ],
            'playgrindergears': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked2.SeqEvent_RemoteEvent_1',
            ],
            're_ep9_thresherdivesbackin': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.thresherIntro.SeqEvent_RemoteEvent_3',
            ],
            're_ep9_threshereatsbeacon': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.thresherIntro.SeqEvent_RemoteEvent_4',
            ],
            're_ep9_threshergrabsbeacon': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.thresherIntro.SeqEvent_RemoteEvent_5',
            ],
            're_ep9_thresherintroend': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.thresherIntro.SeqEvent_RemoteEvent_6',
            ],
            're_turnonloudspeaker': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HyperionLoudspeakerDialog.SeqEvent_RemoteEvent_0',
            ],
            're_ep9_thresherpushessupport1': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.thresherIntro.SeqEvent_RemoteEvent_0',
            ],
            'restartwholething': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqEvent_RemoteEvent_1',
            ],
            'tramready': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqEvent_RemoteEvent_3',
            ],
            'tram_playforward': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqEvent_RemoteEvent_0',
            ],
            'tram_playreverse': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ContainerMoverTrams.SeqEvent_RemoteEvent_2',
            ],
            'turnonthreshers': [
                'Outwash_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_2',
            ],
            'ire_startplayerdistancecheck': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.Scripts_BeaconDefense.SeqEvent_RemoteEvent_0',
            ],
            'ire_stopplayerdistancecheck': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.Scripts_BeaconDefense.SeqEvent_RemoteEvent_2',
            ],
            're_beaconcolloff': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.BeaconManager.SeqEvent_RemoteEvent_0',
            ],
            're_beaconcollon': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.BeaconManager.SeqEvent_RemoteEvent_1',
            ],
            're_closeoffbridgecontrolloader': [
                'Outwash_Dam.TheWorld:PersistentLevel.Main_Sequence.LoaderTakingOutBridgeControls.SeqEvent_RemoteEvent_3',
            ],
            're_destroybridgecontrols': [
                'Outwash_Dam.TheWorld:PersistentLevel.Main_Sequence.LoaderTakingOutBridgeControls.SeqEvent_RemoteEvent_2',
            ],
            're_glutthresherdies': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.thresherIntro.SeqEvent_RemoteEvent_2',
            ],
            're_glutthresherspawns': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.thresherIntro.SeqEvent_RemoteEvent_7',
            ],
            're_lowerbridge': [
                'Outwash_Dam.TheWorld:PersistentLevel.Main_Sequence.LoaderTakingOutBridgeControls.SeqEvent_RemoteEvent_0',
            ],
            're_raisebridge': [
                'Outwash_Dam.TheWorld:PersistentLevel.Main_Sequence.LoaderTakingOutBridgeControls.SeqEvent_RemoteEvent_1',
            ],
            're_startangelhintcountdown': [
                'Outwash_Dam.TheWorld:PersistentLevel.Main_Sequence.AngelCargoMoverHints.SeqEvent_RemoteEvent_4',
            ],
            're_turnoffbridgemissiontrig': [
                'Outwash_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode09.SeqEvent_RemoteEvent_2',
            ],
            're_turnoffgatecombat': [
                'Outwash_Dam.TheWorld:PersistentLevel.Main_Sequence.Combat.SeqEvent_RemoteEvent_0',
            ],
            're_stopangelhints': [
                'Outwash_Dam.TheWorld:PersistentLevel.Main_Sequence.AngelCargoMoverHints.SeqEvent_RemoteEvent_2',
            ],
        },
        'grass_p': {
            'beaconconstructordied': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.CombatControl.SeqEvent_RemoteEvent_1',
            ],
            'beacon_damaged_siren': [
                'Grass_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'beacon_damaged_siren_stop': [
                'Grass_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'destroydave\'shouse': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqEvent_RemoteEvent_1',
            ],
            'ef_killbeacontimers': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.EventControl.SeqEvent_RemoteEvent_3',
            ],
            'ef_pausebeacontimers': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.EventControl.SeqEvent_RemoteEvent_4',
            ],
            'ef_resumebeacontimers': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.EventControl.SeqEvent_RemoteEvent_0',
            ],
            'ere_beacondamaged': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.EventControl.SeqEvent_RemoteEvent_17',
            ],
            'ere_beacontransmitting': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.EventControl.SeqEvent_RemoteEvent_18',
            ],
            'ere_incrementcb': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.EventControl.SeqEvent_RemoteEvent_7',
            ],
            'marcus_radio_music_off': [
                'Grass_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'marcus_radio_music_on': [
                'Grass_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'mothersday_henry50': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MothersDayGift.SeqEvent_RemoteEvent_0',
            ],
            'none': [
                'Grass_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'overlooked3_aimgun': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqEvent_RemoteEvent_4',
            ],
            'overlooked3_aimgun2': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqEvent_RemoteEvent_0',
            ],
            'overlooked3_deploygun': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqEvent_RemoteEvent_3',
            ],
            'overlooked3_turnonshield': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked3.SeqEvent_RemoteEvent_2',
            ],
            'overlooked_guardtakedamage': [
                'Grass_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_0',
                'Grass_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_3',
                'Grass_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_5',
            ],
            'overlooked_karimadoorstart': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_2',
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_3',
            ],
            'overlooked_karimadoorstop': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_4',
            ],
            'overlooked_ropatrol': [
                'Grass_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_7',
            ],
            'overlooked_spawnvendingguards': [
                'Grass_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_6',
            ],
            'overlooked_stopoverlookclockmat': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_1',
            ],
            'overlooked_targetacquired': [
                'Grass_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_1',
                'Grass_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_4',
            ],
            'playgrinder': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked2.SeqEvent_RemoteEvent_0',
            ],
            'playgrindergears': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked2.SeqEvent_RemoteEvent_1',
            ],
            'startoverlookclock': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_0',
            ],
            'turnonthreshers': [
                'Grass_Combat.TheWorld:PersistentLevel.Main_Sequence.Overlooked.SeqEvent_RemoteEvent_2',
            ],
            'ire_startplayerdistancecheck': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.Scripts_BeaconDefense.SeqEvent_RemoteEvent_0',
            ],
            'ire_stopplayerdistancecheck': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.Scripts_BeaconDefense.SeqEvent_RemoteEvent_2',
            ],
            're_beaconcolloff': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.BeaconManager.SeqEvent_RemoteEvent_0',
            ],
            're_beaconcollon': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.BeaconManager.SeqEvent_RemoteEvent_1',
            ],
            're_closingout': [
                'Grass_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DefendTheBeacon.CombatControl.SeqEvent_RemoteEvent_0',
            ],
            're_killbeaconmusicforever': [
                'Grass_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_musicoff': [
                'Grass_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_musicon': [
                'Grass_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
        },
        'luckys_p': {
            'hidesteveinluckys': [
                'Luckys_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'movetotap': [
                'Luckys_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClanWar.SeqEvent_RemoteEvent_0',
            ],
            'teleportbagman': [
                'Luckys_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EndOfRainbow.SeqEvent_RemoteEvent_0',
            ],
        },
        'sage_underground_p': {
            'acquiredtaste_parkvolunteer': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'boatrepairambush': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'bullwarkreset': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'challenge_fishing_complete1': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'dermonstrositat_trapped': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'dropsmasher': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'enabledenatlodge': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'enableundergroundtocliffs': [
                'Sage_Underground_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'enableundergroundtorockforest': [
                'Sage_Underground_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'hammerlockstoprepairing': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'hammerlockgoesbacktolodge': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'hammerlockgoestoboatmachine': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'm1_hammerlockheadstolodge': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'm1_hammerlockmoveinsidelodge': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'm1_hammerlockteleporttolodgecombatlocation': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'm1_teleporthammerlocktoboatslocation': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'rm_etotem': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'rm_etotem2': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'rm_etotem3': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'rm_etotem4': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'sage_m1_hammerlockmovedocks': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'spawnboats': [
                'Sage_Underground_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'teleporthammerlocktobasecamp': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'waitforrepairsload': [
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Sage_Underground_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
        },
        'dead_forest_p': {
            'achieve_swordpullout': [
                'Dead_Forest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'audio_lostsouls_skeleton_transform': [
                'Dead_Forest_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'audio_play_invade_stinger': [
                'Dead_Forest_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'checktospawnswitchandtable': [
                'Dead_Forest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'checktospawnswitchandtable2': [
                'Dead_Forest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'demonicsouls_vo1': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_5',
            ],
            'demonicsouls_vo2': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_6',
            ],
            'demonicsouls_vo3': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_7',
            ],
            'demonicsouls_vo4': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_8',
            ],
            'demonicsouls_vo5': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_9',
            ],
            'demonicsouls_vo6': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_12',
            ],
            'demonicsouls_vo8': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_13',
            ],
            'growferns': [
                'Dead_Forest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'lostsouls_invaderspawned': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_10',
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_4',
            ],
            'lostsouls_sendnpctostart': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_3',
            ],
            'lostsouls_spawninvader': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_2',
            ],
            'lostsouls_spawnknightnpc': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.LostSouls.SeqEvent_RemoteEvent_1',
            ],
            'lostsouls_turnoffcryptdens': [
                'Dead_Forest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'mmorpg_spawndeadknight1': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_3',
            ],
            'mmorpg_spawndeadknight2': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_4',
            ],
            'mmorpg_spawndeadknight3': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_5',
            ],
            'mmo_cancelknightmove/hold': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_19',
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_9',
            ],
            'mmo_knight1revivevo': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_29',
            ],
            'mmo_knight2revivevo': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_28',
            ],
            'mmo_knight3revivevo': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_30',
            ],
            'mmo_makereleaseknightai': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_6',
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_7',
            ],
            'mmo_sendplayerstocampspots': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_8',
            ],
            'mmo_setknight1dq': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_1',
            ],
            'mmo_setknight2dq': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_0',
            ],
            'mmo_setknight3dq': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_2',
            ],
            'mmo_turninvo': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_31',
            ],
            'mmo_turnoffknightpop1': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_16',
            ],
            'mmo_turnoffknightpop2': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_15',
            ],
            'mmo_turnoffknightpop3': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_14',
            ],
            'mmo_turnonknightpop': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_10',
            ],
            'mmo_turnonknightpop1': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_11',
            ],
            'mmo_turnonknightpop2': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_12',
            ],
            'mmo_turnonknightpop3': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_13',
            ],
            'mmo_vo1': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_17',
            ],
            'mmo_vo10': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_27',
            ],
            'mmo_vo2': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_20',
            ],
            'mmo_vo3': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_18',
            ],
            'mmo_vo4': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_21',
            ],
            'mmo_vo5': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_22',
            ],
            'mmo_vo6': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_23',
            ],
            'mmo_vo7': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_24',
            ],
            'mmo_vo8': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_25',
            ],
            'mmo_vo9': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.MMORPGFPS.SeqEvent_RemoteEvent_26',
            ],
            'mre_roll1': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_7',
            ],
            're_cf_roll2': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_0',
            ],
            're_cf_startspinone': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_8',
            ],
            're_cf_startspintwo': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_5',
            ],
            're_cf_tina1stdialog': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_3',
            ],
            're_cf_unhide2': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Critical_Fail.SeqEvent_RemoteEvent_1',
            ],
            're_ghostkingcombatenable': [
                'Dead_Forest_Combat.TheWorld:PersistentLevel.Main_Sequence.GhostKings.SeqEvent_RemoteEvent_0',
            ],
            're_movetorockdeadend': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission02.MeetingGuardScene.SeqEvent_RemoteEvent_0',
            ],
            're_playerhelping': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission02.RolandControls.SeqEvent_RemoteEvent_0',
            ],
            're_prepdragon': [
                'Dead_Forest_Combat.TheWorld:PersistentLevel.Main_Sequence.DragonFight.SeqEvent_RemoteEvent_3',
            ],
            're_putrolandinbattlestate': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission02.RolandControls.SeqEvent_RemoteEvent_5',
            ],
            're_releasedragons': [
                'Dead_Forest_Combat.TheWorld:PersistentLevel.Main_Sequence.DragonFight.SeqEvent_RemoteEvent_1',
            ],
            're_rolandabortmove': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission02.RolandControls.SeqEvent_RemoteEvent_3',
            ],
            're_rolandspawned': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission02.RolandControls.SeqEvent_RemoteEvent_1',
            ],
            're_spellchant': [
                'Dead_Forest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_stopchecks': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission02.RolandControls.SeqEvent_RemoteEvent_2',
            ],
            're_toggleoffgrass': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission02.GhostKingBattle.SeqEvent_RemoteEvent_0',
            ],
            're_turnoffdropdownshield': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission02.GhostKingBattle.SeqEvent_RemoteEvent_1',
            ],
            're_turnondropdownshield': [
                'Dead_Forest_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission02.GhostKingBattle.SeqEvent_RemoteEvent_2',
            ],
        },
        'dungeon_p': {
            'achieve_swordpullout': [
                'Dungeon_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'cancelchallenge': [
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.AngelBossFight.SeqEvent_RemoteEvent_2',
            ],
            'deadbro_11': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_21',
            ],
            'deadbro_12': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_22',
            ],
            'deadbro_turninvo1': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_7',
            ],
            'deadbro_turninvo2': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_8',
            ],
            'deadbro_v10': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_20',
            ],
            'deadbro_vo1': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_9',
            ],
            'deadbro_vo2': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_11',
            ],
            'deadbro_vo3': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_12',
            ],
            'deadbro_vo4': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_14',
            ],
            'deadbro_vo5': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_15',
            ],
            'deadbro_vo6': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_16',
            ],
            'deadbro_vo7': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_17',
            ],
            'deadbro_vo8': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_18',
            ],
            'deadbro_vo9': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_19',
            ],
            'deadbrother_spawnbody1': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_0',
            ],
            'deadbrother_spawnbody2': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_1',
            ],
            'deadbrother_spawnbody3': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_2',
            ],
            'deadbrother_spawnedgar': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_10',
            ],
            'deadbrother_spawnedgarturnin': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_4',
            ],
            'deadbrother_spawnsimon': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_3',
            ],
            'deadbrother_spawnsimonbattle': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_13',
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_6',
            ],
            'deadbrother_spawnsimonbattleturnin': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Dead_Brother.SeqEvent_RemoteEvent_5',
            ],
            'deadbrother_turnoffwizcombat': [
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'forcemizspawn': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.The_Amulet.SeqEvent_RemoteEvent_3',
            ],
            'postcrump_vo6': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.Crumpets.SeqEvent_RemoteEvent_7',
            ],
            're_adn_kickoff': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.The_Amulet.SeqEvent_RemoteEvent_0',
            ],
            're_adn_turnindialog': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.The_Amulet.SeqEvent_RemoteEvent_1',
            ],
            're_asterraid_statueused': [
                'Dungeon_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_purchasedtheamulet': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.The_Amulet.SeqEvent_RemoteEvent_2',
            ],
            're_queencomplete': [
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Dungeon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_raidbosssecretdialogue': [
                'Dungeon_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_toggleendblock': [
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.AngelBossFight.SeqEvent_RemoteEvent_1',
            ],
            're_turnoffwellblocking': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.EnterDungeonScripting.SeqEvent_RemoteEvent_0',
            ],
            're_unlockmainliftshortcut': [
                'Dungeon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_alsosendroland1': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Roland.SeqEvent_RemoteEvent_12',
            ],
            're_angelvoiceinterrup': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.AngelsVoice.SeqEvent_RemoteEvent_10',
            ],
            're_onspiderdeath': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Roland.SeqEvent_RemoteEvent_2',
            ],
            're_openpathwayout': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Outro.SeqEvent_RemoteEvent_0',
            ],
            're_pingenteridle': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Roland.SeqEvent_RemoteEvent_13',
            ],
            're_playerhelping': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Roland.SeqEvent_RemoteEvent_0',
            ],
            're_primewisp1': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.AngelsVoice.SeqEvent_RemoteEvent_8',
            ],
            're_primewisp2': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.AngelsVoice.SeqEvent_RemoteEvent_5',
            ],
            're_primewisp3': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.AngelsVoice.SeqEvent_RemoteEvent_6',
            ],
            're_primewisp4': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.AngelsVoice.SeqEvent_RemoteEvent_7',
            ],
            're_rerunspider': [
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.AngelBossFight.SeqEvent_RemoteEvent_4',
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Outro.SeqEvent_RemoteEvent_4',
            ],
            're_rolandappearkickbutts': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Roland.SeqEvent_RemoteEvent_9',
            ],
            're_rolandappeareddun': [
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_rolandpraiseskill': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Roland.SeqEvent_RemoteEvent_3',
            ],
            're_rolandreact': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Roland.SeqEvent_RemoteEvent_1',
            ],
            're_rolandspawned': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Roland.SeqEvent_RemoteEvent_11',
            ],
            're_spawnangelspider': [
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.AngelBossFight.SeqEvent_RemoteEvent_3',
            ],
            're_spiderqueen_hide': [
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.AngelBossFight.SeqEvent_RemoteEvent_0',
            ],
            're_spiderspawning': [
                'Dungeon_Combat.TheWorld:PersistentLevel.Main_Sequence.AngelBossFight.SeqEvent_RemoteEvent_5',
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.AngelIntroScripting.SeqEvent_RemoteEvent_5',
            ],
            're_stopchecks': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.Roland.SeqEvent_RemoteEvent_4',
            ],
            're_wisppause': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.AngelsVoice.SeqEvent_RemoteEvent_0',
            ],
            're_wispplay': [
                'Dungeon_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission04.AngelsVoice.SeqEvent_RemoteEvent_1',
            ],
            're_enablechest': [
                'Dungeon_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
        },
        'orchid_wormbelly_p': {
            'bosswormdown': [
                'Orchid_WormBelly_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'groundshatter': [
                'Orchid_WormBelly_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'leviathancorpse': [
                'Orchid_WormBelly_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'leviathaninjured': [
                'Orchid_WormBelly_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'music_leviathan_boss_start': [
                'Orchid_WormBelly_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'music_leviathan_boss_stop': [
                'Orchid_WormBelly_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'music_rakkhive_boss_start': [
                'Orchid_WormBelly_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'music_rakkhive_boss_stop': [
                'Orchid_WormBelly_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'piratequeenjumps': [
                'Orchid_WormBelly_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'roscoedead': [
                'Orchid_WormBelly_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'debugcredits': [
                'Orchid_WormBelly_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'debugleviathan': [
                'Orchid_WormBelly_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'debugroscoe': [
                'Orchid_WormBelly_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
        },
        'grass_lynchwood_p': {
            'blowup': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_1',
            ],
            'callbandits': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.KillTheSheriff.SeqEvent_RemoteEvent_3',
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.KillTheSheriff.SeqEvent_RemoteEvent_4',
            ],
            'flare': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.KillTheSheriff.SeqEvent_RemoteEvent_1',
            ],
            'gd_z2_blowthebridgecarthide': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_8',
            ],
            're_activategoons': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.KillTheSheriff.SeqEvent_RemoteEvent_2',
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.KillTheSheriff.SeqEvent_RemoteEvent_6',
            ],
            're_bruiserspawn': [
                'Grass_Lynchwood_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_dukinoatdoghouse': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.SeqEvent_RemoteEvent_9',
            ],
            're_dukinoinsidecave': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.SeqEvent_RemoteEvent_5',
            ],
            're_dukinooutsidecave': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.SeqEvent_RemoteEvent_11',
            ],
            're_enablecavetrigger': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.SeqEvent_RemoteEvent_10',
            ],
            're_noon': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_2',
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_7',
            ],
            're_notnoon': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_4',
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_5',
            ],
            're_resetswitch': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_12',
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_4',
            ],
            're_sitchained': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.Pup.SeqEvent_RemoteEvent_5',
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.Pup.SeqEvent_RemoteEvent_6',
            ],
            're_unlockgrenadeport': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_0',
            ],
            're_spawnloot': [
                'Grass_Lynchwood_Combat.TheWorld:PersistentLevel.Main_Sequence.KillTheSheriff.SeqEvent_RemoteEvent_1',
            ],
            'riderkilled': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_6',
            ],
            'skagzilla2den_movetopoint1': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.SeqEvent_RemoteEvent_1',
            ],
            'skagzilla2pup_stopwalkinghurt': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.Pup.SeqEvent_RemoteEvent_2',
            ],
            'skagzilla2_adultready': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.SeqEvent_RemoteEvent_0',
            ],
            'skagzillapup_feedinganim': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.Pup.SeqEvent_RemoteEvent_0',
            ],
            'starttrain': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_5',
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_7',
            ],
            'startwalking': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.Pup.SeqEvent_RemoteEvent_3',
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.Pup.SeqEvent_RemoteEvent_4',
            ],
            'stopit': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_3',
            ],
            'trainblownup': [
                'Grass_Lynchwood_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_6',
            ],
            'turnonpilesmoke': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BankJob.SeqEvent_RemoteEvent_0',
            ],
            'challengecomplete': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_3',
            ],
            'eatit': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Skagzilla2.Pup.SeqEvent_RemoteEvent_1',
            ],
            'ground': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.KillTheSheriff.SeqEvent_RemoteEvent_5',
            ],
            'playtime': [
                'Grass_Lynchwood_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_debugsheriff': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.KillTheSheriff.SeqEvent_RemoteEvent_0',
            ],
            're_enabletraindude': [
                'Grass_Lynchwood_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_playtrain': [
                'Grass_Lynchwood_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_test': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_1',
            ],
            'spawnguytrain': [
                'Grass_Lynchwood_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'spawndude': [
                'Grass_Lynchwood_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Grass_Lynchwood_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'startit': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_2',
            ],
            'ttrain': [
                'Grass_Lynchwood_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BlowTheBridge.SeqEvent_RemoteEvent_0',
            ],
        },
        'orchid_spire_p': {
            'orchid_activatebeacon': [
                'Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'orchid_endgame_echowontbetrayyou': [
                'Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'orchid_endgame_enableliftlever': [
                'Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'orchid_m8_enableliftlever': [
                'Orchid_Spire_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
        },
        'xmas_p': {
            'boss_fight_music_off': [
                'Xmas_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'boss_fight_music_on': [
                'Xmas_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'close_trainambushdeathvo': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'disableelevator': [
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'enableelevator': [
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'killsnowman_enabletrainfight': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'killsnowman_openwardrobe': [
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'killsnowman_minionwind1': [
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'killsnowman_spawnminions': [
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'marcus_gingertonline': [
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'open_trainambushdeathvo': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_allowrerunnableboss': [
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_allowrunnableloottrain': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_defrostthetown': [
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_disablebossspawnvolumetesting': [
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_removefakewaypoint': [
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_resetlootcarloot': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_settrainoutsidetown': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_spawnsnowman': [
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_statesaver_marcusdoor_open': [
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_statesaver_music_off': [
                'Xmas_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_statesaver_music_on': [
                'Xmas_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_statesaver_trainatambush': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_statesaver_trainatcoaldrop': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_statesaver_trainattowncenter': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_statesaver_trainattownstart': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_statesaver_wardrobe_open': [
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_trainambushspawnminions': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            're_trainambushtocoal': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_trainatambush': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_trainatcoal': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_trainstarttoambush': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_trainstarttoambush_load': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'sendmarcustowardrobe': [
                'XMAS_SIDEMISSION.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'snowboss_hatoff': [
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Xmas_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'snowball_wave0': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'snowball_wave1': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'snowball_wave2': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'snowball_wave3': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'start_failsafetime': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'theftpreventfailed': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'trainambushdeathvo': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'trainfight_movetopoints': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'trainfight_releaseyeti': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'traintheftcleanup': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'trainyetilocked': [
                'Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'train_checkforplayers': [
                'Xmas_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'world_music_on': [
                'Xmas_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'world_music_off': [
                'Xmas_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_yetijumpers': [
                'Xmas_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
        },
        'mines_p': {
            'audio_bad_move': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'audio_claptrap_buff': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'audio_claptrap_debuff': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'audio_claptrap_light_fire': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'audio_golem_emerge_splash': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'audio_good_move': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'audio_greedtooth_dive_in': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'audio_not_raft': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'audio_play_bamf': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'audio_play_punched': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'audio_play_teleport': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'audio_start_golem_bubble': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'audio_start_idle_glow': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'audio_stop_golem_bubble': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'audio_stop_idle_glow': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'claptrapapp_holdisoff': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_14',
            ],
            'claptrapapp_summon1done': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_7',
            ],
            'claptrapapp_teleportclaptrap': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_6',
            ],
            'claptrapapp_activatedebuff': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_9',
            ],
            'claptrapapp_claptrapvanishsfx': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_20',
            ],
            'claptrapapp_holdison': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_13',
            ],
            'claptrapapp_moveclaptostart': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_2',
            ],
            'claptrapapp_playerinarea': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_8',
            ],
            'claptrapapp_removedebuff': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_10',
            ],
            'claptrapapp_spawnbroom2': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_4',
            ],
            'claptrapapp_spawnbroom3and4': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_5',
            ],
            'claptrapapp_startfollowvo': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_38',
            ],
            'claptrapapp_startingmove1': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_1',
            ],
            'claptrapapp_startingmove2': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_11',
            ],
            'claptrapapp_turninvo': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_39',
            ],
            'claptrapapp_turnoffbuttonglow': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_10',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_8',
            ],
            'claptrapapp_turnoffblockingvolumes': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_2',
            ],
            'claptrapapp_turnoffbrooms': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_15',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_3',
            ],
            'claptrapapp_turnoffcombatdens': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'claptrapapp_turnoffstorm': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Mines_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'claptrapapp_turnonbuttonglow': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_7',
            ],
            'claptrapapp_turnoncombatdens': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'claptrapapp_turnonfire': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_12',
            ],
            'claptrapapp_turnonstorm': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Mines_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_0',
            ],
            'claptrapapp_vo18': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_43',
            ],
            'claptrapapp_vo1e': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_40',
            ],
            'claptrapapp_volive1': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_16',
            ],
            'claptrapapp_volive2': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_17',
            ],
            'claptrapapp_volive3': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_18',
            ],
            'claptrapapp_volive4': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_App.SeqEvent_RemoteEvent_19',
            ],
            'claptrapbeard_beardfloat': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_1',
            ],
            'claptrapbeard_beardfloat_load': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_3',
            ],
            'claptrapbeard_beardpiecesviz': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_9',
            ],
            'claptrapbeard_lowerhammer': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_4',
            ],
            'claptrapbeard_moveforgeout': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_0',
            ],
            'claptrapbeard_sendhammerback': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_5',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_6',
            ],
            'claptrapbeard_strikeforgemat': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_2',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_21',
            ],
            'claptrapbeard_turninvo': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_14',
            ],
            'claptrapbeard_vo10': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_20',
            ],
            'claptrapbeard_vo11': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_22',
            ],
            'claptrapbeard_vo12': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_23',
            ],
            'claptrapbeard_vo13': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_25',
            ],
            'claptrapbeard_vo4': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_15',
            ],
            'claptrapbeard_vo6': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_16',
            ],
            'claptrapbeard_vo7': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_17',
            ],
            'claptrapbeard_vo8': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_18',
            ],
            'claptrapbeard_vo9': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Beard.SeqEvent_RemoteEvent_19',
            ],
            'claptrapwand_spawngolem': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_8',
            ],
            'claptrapwand_spawnorc': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_1',
            ],
            'claptrapwand_spawnspider': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_0',
            ],
            'claptrapwand_vo10': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_29',
            ],
            'claptrapwand_vo11': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_34',
            ],
            'claptrapwand_vo12': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_35',
            ],
            'claptrapwand_vo13': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_36',
            ],
            'claptrapwand_vo14': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_37',
            ],
            'claptrapwand_vo15': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_33',
            ],
            'claptrapwand_vo16': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_3',
            ],
            'claptrapwand_vo2': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_27',
            ],
            'claptrapwand_vo4': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_28',
            ],
            'claptrapwand_vo5': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_30',
            ],
            'claptrapwand_vo7': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_31',
            ],
            'claptrapwand_vo9': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_32',
            ],
            'claptrapwand_voturnin': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Claptrap_Wand.SeqEvent_RemoteEvent_26',
            ],
            'drop': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'lock': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'mission3_teleportclaptoplatform': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_9',
            ],
            'postcrump_vo5': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Crumpets.SeqEvent_RemoteEvent_5',
            ],
            're_activateteleports': [
                'Mines_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_7',
            ],
            're_bossbar': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            're_bossresetcheck': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_bossstopresetcheck': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            're_claptrapmovetorune': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_2',
            ],
            're_claptraprunetaken': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_13',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_6',
            ],
            're_continuepuzzle': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_18',
            ],
            're_coreattach': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreAttach.SeqEvent_RemoteEvent_0',
            ],
            're_coreidlespin_start': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqEvent_RemoteEvent_16',
            ],
            're_coreidlespin_stop': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqEvent_RemoteEvent_12',
            ],
            're_coremovementdisplayrune': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqEvent_RemoteEvent_9',
            ],
            're_coremovementlower': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqEvent_RemoteEvent_10',
            ],
            're_coremovementraise': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqEvent_RemoteEvent_15',
            ],
            're_coremovementstart': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqEvent_RemoteEvent_8',
            ],
            're_cubelocupdate_x1': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX1_Right.SeqEvent_RemoteEvent_3',
            ],
            're_cubelocupdate_x3': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX3_Left.SeqEvent_RemoteEvent_3',
            ],
            're_cubelocupdate_y1': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY1_Right.SeqEvent_RemoteEvent_3',
            ],
            're_cubelocupdate_y3': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY3_Left.SeqEvent_RemoteEvent_3',
            ],
            're_cubelocupdate_z1': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ1_Right.SeqEvent_RemoteEvent_3',
            ],
            're_cubelocupdate_z3': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ3_Left.SeqEvent_RemoteEvent_3',
            ],
            're_disablepuzzleswitches': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_23',
            ],
            're_disablestartupswitches': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_15',
            ],
            're_enablestartupswitches': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_19',
            ],
            're_extendbridge': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_18',
            ],
            're_farspawn': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_farstop': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_finishpuzzle': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.CoreMovement.SeqEvent_RemoteEvent_3',
            ],
            're_ggdead': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_ggdeath': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            're_ggreset': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_gearf1used_solve': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_6',
            ],
            're_gearf1used_startup': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_12',
            ],
            're_gearf2used_solve': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_7',
            ],
            're_gearf2used_startup': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_13',
            ],
            're_gearl1used_solve': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_2',
            ],
            're_gearl1used_startup': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_0',
            ],
            're_gearl2used_solve': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_3',
            ],
            're_gearl2used_startup': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_9',
            ],
            're_gearr1used_solve': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_4',
            ],
            're_gearr1used_startup': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_10',
            ],
            're_gearr2used_solve': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_5',
            ],
            're_gearr2used_startup': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_11',
            ],
            're_goldgolemstage1': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_greedtoothrunetaken': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_15',
            ],
            're_groundimpactl': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_groundimpactlspawn': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_groundimpactr': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_groundimpactrspawn': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_jumpingpuzzlecomplete': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_4',
            ],
            're_jumpingrunetaken': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_16',
            ],
            're_localreset_x1': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX1_Right.SeqEvent_RemoteEvent_2',
            ],
            're_localreset_x3': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX3_Left.SeqEvent_RemoteEvent_2',
            ],
            're_localreset_y1': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY1_Right.SeqEvent_RemoteEvent_2',
            ],
            're_localreset_y3': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY3_Left.SeqEvent_RemoteEvent_2',
            ],
            're_localreset_z1': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ1_Right.SeqEvent_RemoteEvent_2',
            ],
            're_localreset_z3': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ3_Left.SeqEvent_RemoteEvent_2',
            ],
            're_lowergreedtoothfence': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_11',
            ],
            're_mineexitlocked': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_8',
            ],
            're_nextpuzzleturn': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_1',
            ],
            're_pausematinee': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            're_puzzlebroken': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_3',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_17',
            ],
            're_puzzlerunetaken': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_17',
            ],
            're_puzzlesolved': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_20',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_21',
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_22',
            ],
            're_queueuplongjump': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_ragnaradds': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_raisegreedtoothfence': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_10',
            ],
            're_setuppuzzle': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_1',
            ],
            're_spokeraft': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_0',
            ],
            're_startgolemcombat': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_startjumpingpuzzle': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_19',
            ],
            're_startuppuzzle': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_8',
            ],
            're_teleportused': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_12',
            ],
            're_triggerroadblockcollapse': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_5',
            ],
            're_turnx1_right': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX1_Right.SeqEvent_RemoteEvent_1',
            ],
            're_turnx1_right_reset': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX1_Right.SeqEvent_RemoteEvent_0',
            ],
            're_turnx3_left': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX3_Left.SeqEvent_RemoteEvent_1',
            ],
            're_turnx3_left_reset': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnX3_Left.SeqEvent_RemoteEvent_0',
            ],
            're_turny1_right': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY1_Right.SeqEvent_RemoteEvent_1',
            ],
            're_turny1_right_reset': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY1_Right.SeqEvent_RemoteEvent_0',
            ],
            're_turny3_left': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY3_Left.SeqEvent_RemoteEvent_1',
            ],
            're_turny3_left_reset': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnY3_Left.SeqEvent_RemoteEvent_0',
            ],
            're_turnz1_right': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ1_Right.SeqEvent_RemoteEvent_1',
            ],
            're_turnz1_right_reset': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ1_Right.SeqEvent_RemoteEvent_0',
            ],
            're_turnz3_left': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ3_Left.SeqEvent_RemoteEvent_1',
            ],
            're_turnz3_left_reset': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.TurnZ3_Left.SeqEvent_RemoteEvent_0',
            ],
            're_unwindpuzzle': [
                'Mines_Mission.TheWorld:PersistentLevel.Main_Sequence.Episode_3.DwarvenPuzzle.SeqEvent_RemoteEvent_16',
            ],
            're_volleydone': [
                'Mines_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'spiderpants': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'unlock': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'gotime': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'rockguy': [
                'Mines_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
        },
        'templeslaughter_p': {
            'achieve_swordpullout': [
                'TempleSlaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_15secft': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.floortraps.SeqEvent_RemoteEvent_1',
            ],
            're_30secft': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.floortraps.SeqEvent_RemoteEvent_2',
            ],
            're_blb_ab_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_26',
            ],
            're_blb_ab_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_27',
            ],
            're_blb_ab_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_29',
            ],
            're_blb_ab_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_28',
            ],
            're_blb_a_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_72',
            ],
            're_blb_a_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_73',
            ],
            're_blb_a_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_75',
            ],
            're_blb_a_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_74',
            ],
            're_blb_bc_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_12',
            ],
            're_blb_bc_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_13',
            ],
            're_blb_bc_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_2',
            ],
            're_blb_bc_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_3',
            ],
            're_blb_b_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_18',
            ],
            're_blb_b_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_19',
            ],
            're_blb_b_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_21',
            ],
            're_blb_b_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_20',
            ],
            're_blb_cd_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_14',
            ],
            're_blb_cd_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_15',
            ],
            're_blb_cd_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_17',
            ],
            're_blb_cd_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_16',
            ],
            're_blb_c_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_6',
            ],
            're_blb_c_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_7',
            ],
            're_blb_c_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_9',
            ],
            're_blb_c_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_8',
            ],
            're_blb_d_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_208',
            ],
            're_blb_d_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_209',
            ],
            're_blb_d_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_211',
            ],
            're_blb_d_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_210',
            ],
            're_blb_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_68',
            ],
            're_blb_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_69',
            ],
            're_bmp_a_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_217',
            ],
            're_bmp_a_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_216',
            ],
            're_bmp_b_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_35',
            ],
            're_bmp_b_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_34',
            ],
            're_bmp_c_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_32',
            ],
            're_bmp_c_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_33',
            ],
            're_bmp_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_11',
            ],
            're_bmp_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_10',
            ],
            're_brb_ab_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_96',
            ],
            're_brb_ab_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_97',
            ],
            're_brb_ab_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_99',
            ],
            're_brb_ab_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_98',
            ],
            're_brb_ad_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_103',
            ],
            're_brb_ad_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_102',
            ],
            're_brb_ad_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_100',
            ],
            're_brb_ad_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_101',
            ],
            're_brb_a_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_95',
            ],
            're_brb_a_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_94',
            ],
            're_brb_a_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_92',
            ],
            're_brb_a_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_93',
            ],
            're_brb_b_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_88',
            ],
            're_brb_b_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_89',
            ],
            're_brb_b_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_91',
            ],
            're_brb_b_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_90',
            ],
            're_brb_cd_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_59',
            ],
            're_brb_cd_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_58',
            ],
            're_brb_cd_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_56',
            ],
            're_brb_cd_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_57',
            ],
            're_brb_c_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_67',
            ],
            're_brb_c_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_66',
            ],
            're_brb_c_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_64',
            ],
            're_brb_c_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_65',
            ],
            're_brb_d_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_60',
            ],
            're_brb_d_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_61',
            ],
            're_brb_d_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_63',
            ],
            're_brb_d_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_62',
            ],
            're_brb_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_55',
            ],
            're_brb_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Bot.SeqEvent_RemoteEvent_54',
            ],
            're_bigdoor': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Misc.SeqEvent_RemoteEvent_1',
            ],
            're_bigdoor_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Misc.SeqEvent_RemoteEvent_2',
            ],
            're_bottomvents': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.floortraps.SeqEvent_RemoteEvent_4',
            ],
            're_checkplayers': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.TempleTower.SeqEvent_RemoteEvent_0',
            ],
            're_mid_ab_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_111',
            ],
            're_mid_ab_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_110',
            ],
            're_mid_ab_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_108',
            ],
            're_mid_ab_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_109',
            ],
            're_mid_ad_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_104',
            ],
            're_mid_ad_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_105',
            ],
            're_mid_ad_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_107',
            ],
            're_mid_ad_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_106',
            ],
            're_mid_a_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_112',
            ],
            're_mid_a_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_113',
            ],
            're_mid_a_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_115',
            ],
            're_mid_a_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_114',
            ],
            're_mid_bc_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_53',
            ],
            're_mid_bc_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_52',
            ],
            're_mid_bc_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_50',
            ],
            're_mid_bc_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_51',
            ],
            're_mid_b_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_119',
            ],
            're_mid_b_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_118',
            ],
            're_mid_b_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_116',
            ],
            're_mid_b_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_117',
            ],
            're_mid_cd_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_46',
            ],
            're_mid_cd_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_47',
            ],
            're_mid_cd_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_49',
            ],
            're_mid_cd_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_48',
            ],
            're_mid_c_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_38',
            ],
            're_mid_c_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_39',
            ],
            're_mid_c_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_41',
            ],
            're_mid_c_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_40',
            ],
            're_mid_d_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_45',
            ],
            're_mid_d_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_44',
            ],
            're_mid_d_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_42',
            ],
            're_mid_d_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_43',
            ],
            're_mlb_a_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_121',
            ],
            're_mlb_a_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_120',
            ],
            're_mlb_a_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_127',
            ],
            're_mlb_a_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_126',
            ],
            're_mlb_a_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_124',
            ],
            're_mlb_a_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_125',
            ],
            're_mlb_b_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_122',
            ],
            're_mlb_b_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_123',
            ],
            're_mlb_b_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_128',
            ],
            're_mlb_b_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_129',
            ],
            're_mlb_b_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_131',
            ],
            're_mlb_b_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_130',
            ],
            're_mlb_c_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_135',
            ],
            're_mlb_c_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_134',
            ],
            're_mlb_c_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_132',
            ],
            're_mlb_c_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_133',
            ],
            're_mlb_d_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_136',
            ],
            're_mlb_d_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_137',
            ],
            're_mlb_d_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_139',
            ],
            're_mlb_d_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_138',
            ],
            're_mrb_a_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_71',
            ],
            're_mrb_a_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_70',
            ],
            're_mrb_a_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_83',
            ],
            're_mrb_a_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_82',
            ],
            're_mrb_a_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_80',
            ],
            're_mrb_a_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_81',
            ],
            're_mrb_b_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_31',
            ],
            're_mrb_b_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_30',
            ],
            're_mrb_b_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_84',
            ],
            're_mrb_b_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_85',
            ],
            're_mrb_b_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_87',
            ],
            're_mrb_b_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_86',
            ],
            're_mrb_c_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_25',
            ],
            're_mrb_c_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_24',
            ],
            're_mrb_c_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_22',
            ],
            're_mrb_c_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_23',
            ],
            're_mrb_d_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_79',
            ],
            're_mrb_d_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_78',
            ],
            're_mrb_d_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_76',
            ],
            're_mrb_d_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Middle.SeqEvent_RemoteEvent_77',
            ],
            're_openbotpits': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_10',
            ],
            're_openbotpits_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_14',
            ],
            're_openpits': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_12',
            ],
            're_openpits_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_9',
            ],
            're_reverseall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Misc.SeqEvent_RemoteEvent_0',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotems.SeqEvent_RemoteEvent_1',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.The_Crystal_Structure.SeqEvent_RemoteEvent_1',
            ],
            're_raisetower': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.TempleTower.SeqEvent_RemoteEvent_2',
            ],
            're_randombottomtotems': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_16',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_17',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_18',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_19',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_20',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_21',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_22',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_3',
            ],
            're_randombottomtotems_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_15',
            ],
            're_randompits': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotems.SeqEvent_RemoteEvent_0',
            ],
            're_randomtotemtraps': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotems.SeqEvent_RemoteEvent_2',
            ],
            're_randomtotemswithwalls': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_2',
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_23',
            ],
            're_randomvents': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.floortraps.SeqEvent_RemoteEvent_0',
            ],
            're_stands_a_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_231',
            ],
            're_stands_a_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_230',
            ],
            're_stands_a_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_247',
            ],
            're_stands_a_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_246',
            ],
            're_stands_a_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_244',
            ],
            're_stands_a_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_245',
            ],
            're_stands_b_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_252',
            ],
            're_stands_b_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_253',
            ],
            're_stands_b_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_224',
            ],
            're_stands_b_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_225',
            ],
            're_stands_b_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_227',
            ],
            're_stands_b_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_226',
            ],
            're_stands_c_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_248',
            ],
            're_stands_c_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_249',
            ],
            're_stands_c_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_251',
            ],
            're_stands_c_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_250',
            ],
            're_stands_d_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_228',
            ],
            're_stands_d_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_229',
            ],
            're_stands_d_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_223',
            ],
            're_stands_d_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_222',
            ],
            're_stands_d_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_220',
            ],
            're_stands_d_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Stands.SeqEvent_RemoteEvent_221',
            ],
            're_skycrystal': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.The_Crystal_Structure.SeqEvent_RemoteEvent_0',
            ],
            're_skycrystal_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.The_Crystal_Structure.SeqEvent_RemoteEvent_2',
            ],
            're_spawnswithwallsa': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotems.SeqEvent_RemoteEvent_3',
            ],
            're_spawnswithwallsa_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotems.SeqEvent_RemoteEvent_8',
            ],
            're_tlb_ab_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_143',
            ],
            're_tlb_ab_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_142',
            ],
            're_tlb_ab_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_140',
            ],
            're_tlb_ab_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_141',
            ],
            're_tlb_a_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_144',
            ],
            're_tlb_a_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_145',
            ],
            're_tlb_a_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_147',
            ],
            're_tlb_a_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_146',
            ],
            're_tlb_bc_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_152',
            ],
            're_tlb_bc_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_153',
            ],
            're_tlb_bc_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_155',
            ],
            're_tlb_bc_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_154',
            ],
            're_tlb_b_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_151',
            ],
            're_tlb_b_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_150',
            ],
            're_tlb_b_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_148',
            ],
            're_tlb_b_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_149',
            ],
            're_tlb_cd_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_166',
            ],
            're_tlb_cd_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_167',
            ],
            're_tlb_cd_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_169',
            ],
            're_tlb_cd_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_168',
            ],
            're_tlb_c_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_158',
            ],
            're_tlb_c_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_159',
            ],
            're_tlb_c_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_161',
            ],
            're_tlb_c_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_160',
            ],
            're_tlb_d_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_165',
            ],
            're_tlb_d_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_164',
            ],
            're_tlb_d_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_162',
            ],
            're_tlb_d_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_163',
            ],
            're_tlb_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_156',
            ],
            're_tlb_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_157',
            ],
            're_tmp_a_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_176',
            ],
            're_tmp_a_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_177',
            ],
            're_tmp_b_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_175',
            ],
            're_tmp_b_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_174',
            ],
            're_tmp_c_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_172',
            ],
            're_tmp_c_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_173',
            ],
            're_tmp_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_171',
            ],
            're_tmp_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_170',
            ],
            're_trb_ab_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_188',
            ],
            're_trb_ab_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_189',
            ],
            're_trb_ab_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_191',
            ],
            're_trb_ab_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_190',
            ],
            're_trb_ad_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_195',
            ],
            're_trb_ad_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_194',
            ],
            're_trb_ad_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_192',
            ],
            're_trb_ad_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_193',
            ],
            're_trb_a_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_187',
            ],
            're_trb_a_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_186',
            ],
            're_trb_a_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_184',
            ],
            're_trb_a_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_185',
            ],
            're_trb_b_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_178',
            ],
            're_trb_b_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_179',
            ],
            're_trb_b_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_181',
            ],
            're_trb_b_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_180',
            ],
            're_trb_cd_fullwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_199',
            ],
            're_trb_cd_fullwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_198',
            ],
            're_trb_cd_halflwall': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_196',
            ],
            're_trb_cd_halflwall_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_197',
            ],
            're_trb_c_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_207',
            ],
            're_trb_c_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_206',
            ],
            're_trb_c_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_204',
            ],
            're_trb_c_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_205',
            ],
            're_trb_d_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_200',
            ],
            're_trb_d_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_201',
            ],
            're_trb_d_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_203',
            ],
            're_trb_d_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_202',
            ],
            're_trb_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_183',
            ],
            're_trb_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Top.SeqEvent_RemoteEvent_182',
            ],
            're_totemsstands': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_7',
            ],
            're_totemsstands_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_11',
            ],
            're_totemsupper': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_13',
            ],
            're_totemsupper_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotemsB.SeqEvent_RemoteEvent_6',
            ],
            're_totemswithwallsa': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotems.SeqEvent_RemoteEvent_4',
            ],
            're_totemswithwallsb': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.RandomTotems.SeqEvent_RemoteEvent_5',
            ],
            're_upper_a_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_228',
            ],
            're_upper_a_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_229',
            ],
            're_upper_a_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_223',
            ],
            're_upper_a_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_222',
            ],
            're_upper_a_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_220',
            ],
            're_upper_a_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_221',
            ],
            're_upper_b_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_231',
            ],
            're_upper_b_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_230',
            ],
            're_upper_b_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_224',
            ],
            're_upper_b_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_225',
            ],
            're_upper_b_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_227',
            ],
            're_upper_b_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_226',
            ],
            're_upper_c_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_218',
            ],
            're_upper_c_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_219',
            ],
            're_upper_c_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_215',
            ],
            're_upper_c_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_214',
            ],
            're_upper_c_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_212',
            ],
            're_upper_c_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_213',
            ],
            're_upper_d_pit': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_36',
            ],
            're_upper_d_pit_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_37',
            ],
            're_upper_d_spawn': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_4',
            ],
            're_upper_d_spawn_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_5',
            ],
            're_upper_d_totem': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_1',
            ],
            're_upper_d_totem_rev': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.Upper.SeqEvent_RemoteEvent_0',
            ],
            're_upperstandsvents': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.floortraps.SeqEvent_RemoteEvent_5',
            ],
            're_lowertower': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.TempleTower.SeqEvent_RemoteEvent_1',
            ],
            'rm_explosiontower': [
                'TempleSlaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.TempleTower.SeqEvent_RemoteEvent_3',
            ],
        },
        'creatureslaughter_p': {
            'door_l': [
                'CreatureSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'door_r': [
                'CreatureSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'sidedoors': [
                'CreatureSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'smalldoor_l': [
                'CreatureSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'smalldoor_r': [
                'CreatureSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ultimatebug_attack': [
                'CreatureSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Stage2.SeqEvent_RemoteEvent_2',
            ],
            'ultimatebug_retreat': [
                'CreatureSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Stage2.SeqEvent_RemoteEvent_1',
            ],
        },
        'orchid_oasistown_p': {
            'buryingpast_detonate': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'orchid_m1_turnin': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'orchid_m2_destroyskiff': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'orchid_m2_kickoff': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'orchid_m2_partfound': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'orchid_m2_partscollected': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'orchid_m2_skiffscanned': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'orchid_m2_turnin': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'orchid_m2_usedskiff': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'orchid_m3_kickoff': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'orchid_sm_firewater_kickoff': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'orchid_sm_firewater_returnshade': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            'orchid_sm_jockolegup_kickoff': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'orchid_sm_jockolegup_turnin': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'orchid_sm_messagebottle_foundloot': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'orchid_sm_messagebottle_kickoff': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'orchid_sm_messagebottle_turnin': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'orchid_sm_wingman_completed': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'orchid_sm_wingman_kickoff': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'rm_turnofmore': [
                'Orchid_OasisTown_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'debugqueen': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Mission02WormQueen.SeqEvent_RemoteEvent_0',
            ],
            'debugshade': [
                'Orchid_OasisTown_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ShadeTitleCard.SeqEvent_RemoteEvent_0',
            ],
        },
        'hyperioncity_p': {
            'activateturretszone1': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'callloaders': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'doubleweak': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'ere_startmoonshot_1': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_1',
            ],
            'ere_startmoonshot_2': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_2',
            ],
            'ere_startmoonshot_3': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_0',
            ],
            'ep12_stoptimer': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'flood_audio': [
                'HyperionCity_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'HyperionCity_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'HyperionCity_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'HyperionCity_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'foremancreatedturret': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HellHathNoFury.SeqEvent_RemoteEvent_1',
            ],
            'homemovies_playing': [
                'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Earthquake.SeqEvent_RemoteEvent_1',
            ],
            'homemovies_sendprobeagain': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HomeMovies.SeqEvent_RemoteEvent_3',
            ],
            'homemovies_startbackuptimer': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HomeMovies.backupTimer.SeqEvent_RemoteEvent_2',
            ],
            'homemovies_stopbackuptimer': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HomeMovies.backupTimer.SeqEvent_RemoteEvent_5',
            ],
            'homemovies_stopped': [
                'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Earthquake.SeqEvent_RemoteEvent_2',
            ],
            'm_homemovies_launchorbital': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HomeMovies.Crane.SeqEvent_RemoteEvent_1',
            ],
            'reset1': [
                'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_1',
            ],
            'reset2': [
                'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_2',
            ],
            'reset3': [
                'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_3',
            ],
            'reset4': [
                'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_0',
            ],
            'sendprobe': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HomeMovies.SeqEvent_RemoteEvent_0',
            ],
            'statue1combatcomplete': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_3',
            ],
            'statue2combatcomplete': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_4',
            ],
            'statue3combatcomplete': [
                'HyperionCity_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_5',
            ],
            'turnoffstatue4den': [
                'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_4',
            ],
            'turnonstatue4den': [
                'HyperionCity_P.TheWorld:PersistentLevel.Main_Sequence.Statues.SeqEvent_RemoteEvent_5',
            ],
        },
        'robotslaughter_p': {
            'closeelecator': [
                'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'dropshipenter': [
                'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'dropshipexit': [
                'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'enter_dropzone': [
                'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'enter_lava': [
                'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'enter_mines': [
                'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'openelevator': [
                'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'toggleconfetti': [
                'RobotSlaughter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
        },
        'iris_dl2_interior_p': {
            'activatepetelift': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'clearbarfight': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'dl1_unhidemoxie': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'ep3battle_barcomplete': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'ep3battle_barcomplete2': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'ep3battle_barcomplete3': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'iris_barfight_hasmission': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'iris_barfight_reopen': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'iris_barroom_playerspawned': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'iris_dl2int_restbar': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'iris_headformoxxiesmontage': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'iris_peteelevatoron': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'iris_raid1_checklockout': [
                'Iris_DL2_Interior_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'iris_updatetheboard': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'm_chopsuey_started': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'pyropeteintrofinished': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'pyropetespawned': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'raidpete_player01_assigned': [
                'Iris_DL2_Interior_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'raidpete_player02_assigned': [
                'Iris_DL2_Interior_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'raidpete_player03_assigned': [
                'Iris_DL2_Interior_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'raidpete_player04_assigned': [
                'Iris_DL2_Interior_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'raidpyropetespawned': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'raid_pyropete_killed': [
                'Iris_DL2_Interior_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'resetnormalpetefight': [
                'Iris_DL2_Interior_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'setbattle_barfight': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'setbattle_barfight2': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'setbattle_barfight3': [
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
                'Iris_DL2_Interior_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'setbattle_barfightdoors': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'spawnwave1': [
                'Iris_DL2_Interior_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'spawnwave2': [
                'Iris_DL2_Interior_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'start bar fight music': [
                'Iris_DL2_Interior_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'start pyro music': [
                'Iris_DL2_Interior_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'stop bar fight music': [
                'Iris_DL2_Interior_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'stop pyro music': [
                'Iris_DL2_Interior_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'debugmoxxi': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'debugpyro': [
                'Iris_DL2_Interior_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
        },
        'testingzone_p': {
            'assembledobj': [
                'TESTINGZONE_COMBAT.TheWorld:PersistentLevel.Main_Sequence.TestingZone.SeqEvent_RemoteEvent_1',
            ],
            'lockplayerin': [
                'TESTINGZONE_COMBAT.TheWorld:PersistentLevel.Main_Sequence.Second_Combat_Area.SeqEvent_RemoteEvent_0',
            ],
            'rm_addonions': [
                'TESTINGZONE_COMBAT.TheWorld:PersistentLevel.Main_Sequence.TestingZone.SeqEvent_RemoteEvent_2',
            ],
            'rm_closeunlockdoordoor': [
                'TESTINGZONE_COMBAT.TheWorld:PersistentLevel.Main_Sequence.TestingZone.SeqEvent_RemoteEvent_3',
                'TESTINGZONE_COMBAT.TheWorld:PersistentLevel.Main_Sequence.Unlock_Door.SeqEvent_RemoteEvent_0',
            ],
            'rm_firsttrainleave': [
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'rm_firsttrainstart': [
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'rm_secondtrainleave': [
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'rm_secondtrainstart': [
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'rm_shieldsdeployed': [
                'TestingZone_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'rm_shieldsnotdeployed': [
                'TestingZone_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'slaughter_music_start': [
                'TestingZone_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'slaughter_music_stop': [
                'TestingZone_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'unlockdoorobj': [
                'TESTINGZONE_COMBAT.TheWorld:PersistentLevel.Main_Sequence.Unlock_Door.SeqEvent_RemoteEvent_1',
            ],
            're_audio_speedingup': [
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.Train.SeqEvent_RemoteEvent_3',
            ],
            're_audio_trainreachedfullspeed': [
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.Train.SeqEvent_RemoteEvent_2',
            ],
            're_audio_trainslowing': [
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.Train.SeqEvent_RemoteEvent_0',
            ],
            're_audio_trainstopped': [
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.Train.SeqEvent_RemoteEvent_1',
            ],
            're_destroyturrets': [
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.Train.SeqEvent_RemoteEvent_5',
                'TESTINGZONE_DYNAMIC.TheWorld:PersistentLevel.Main_Sequence.Train.SeqEvent_RemoteEvent_6',
            ],
        },
        'distillery_p': {
            'aborttrailerjump': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'audio_play_wavecrash': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'boss_fight_music_off': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'boss_fight_music_on': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'bottle_pour_audio': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'bridejumptotrailer': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'debugmessage_babycrying': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.Debug.SeqEvent_RemoteEvent_4',
            ],
            'debugmessage_needstobelive': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.Debug.SeqEvent_RemoteEvent_5',
            ],
            'debugmessage_whyaretheysomad': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.Debug.SeqEvent_RemoteEvent_7',
            ],
            'glowbaby': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_0',
            ],
            'groomjumptotrailer': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'lightningflash1': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'lightningflash2': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'lightningflash3': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'lightningflash4': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'lightning_flash_audio': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'loaderintro_done': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.DistilleryCombat_LoaderChase.SeqEvent_RemoteEvent_0',
            ],
            're_activategroomsmanencounter': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.DistilleryCombat.SeqEvent_RemoteEvent_2',
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_aggrostella': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            're_agrojunkbot': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_allowchurchchests': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_allowrerunnableboss': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_awfulsaveloadhack': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_awfulsaveloadhack2': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_awfulsaveloadhack3': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_churchbells': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_cigarpickedup': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_destroybabygatemoxxi': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_disablebosselevator': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_disablebossspawnvolumetesting': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_distilerygaragedoor_close': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_0',
            ],
            're_distilerygaragedoor_open': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_6',
            ],
            're_enablebosselevator': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_fliphodnkallegiancesidemission': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.KillHodunksCombat.SeqEvent_RemoteEvent_9',
            ],
            're_greasepickedup': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_8',
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_lightning_flash_fx': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_makegloomy': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_makesunny': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_moxxiteaserdialog': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_prepwedding': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_removefakewaypoint': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_sidemission_despawnlilah': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_sidemission_despawnmoxxi': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_13',
            ],
            're_sidemission_despawnnate': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_sidemission_spawnlilah': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_sidemission_spawnmoxxi': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_10',
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_8',
            ],
            're_sidemission_spawnnate': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_spawnbabygatemoxxi': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_spawnhotairballoon': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_spawninnuendobot_final': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_startgoliathfight': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_startstormy': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_startwedding': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_statesaver_music_off': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_statesaver_music_on': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_stopstormy': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_storyendingdialog': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_testibotleave': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'sidemissionteaser': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'start_distill_audio': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'stop_distill_audio': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'stop_fan_audio': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'testenddialog': [
                'Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'world_music_on': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'world_music_off': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_addwaypointtobaby': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_8',
            ],
            're_addwaypointtovat': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_3',
            ],
            're_ambientargument1': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.Arguments.SeqEvent_RemoteEvent_2',
            ],
            're_ambientargument2': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.Arguments.SeqEvent_RemoteEvent_1',
            ],
            're_babystartscooing': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_banjo_audio_off': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_banjo_audio_on': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_bashwall': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.WhiskeyDrinking.SeqEvent_RemoteEvent_0',
            ],
            're_botspawned': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_1',
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.RobotSetupSequences.SeqEvent_RemoteEvent_1',
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.RobotSetupSequences.SeqEvent_RemoteEvent_10',
            ],
            're_bridgeandgroomtalkedto': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.SeqEvent_RemoteEvent_1',
            ],
            're_callouttostelladialog': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_5',
            ],
            're_closemoxxiedoors': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_3',
            ],
            're_closeoffzafpissedoffdialog': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.DistilleryCombat.SeqEvent_RemoteEvent_0',
            ],
            're_couplegone_spawnjloaderatgate': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.RobotSetupSequences.SeqEvent_RemoteEvent_0',
            ],
            're_despawnibot': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.SeqEvent_RemoteEvent_0',
            ],
            're_despawnintromoxxie': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_2',
            ],
            're_despawnnate': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.ThresherCombat.SeqEvent_RemoteEvent_3',
            ],
            're_drinkholdoff': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.WhiskeyDrinking.SeqEvent_RemoteEvent_7',
            ],
            're_drinkholdon': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.WhiskeyDrinking.SeqEvent_RemoteEvent_8',
            ],
            're_enableonloadjunkbotkickoff': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_8',
            ],
            're_endallchecks': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_2',
            ],
            're_fliptownpercherallegience': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.KillHodunksCombat.SeqEvent_RemoteEvent_1',
            ],
            're_hidemoxxiespeaker': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_1',
            ],
            're_hidesidebottle': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.WhiskeyDrinking.SeqEvent_RemoteEvent_4',
            ],
            're_innerdooropenedbybot': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.RobotSetupSequences.SeqEvent_RemoteEvent_14',
            ],
            're_moxxiecomments': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.GoldenLoader.SeqEvent_RemoteEvent_0',
            ],
            're_moxxieopensgateweatherchange_startmusic': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_moxxierejectgift': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_19',
            ],
            're_noreallypleasebeoff': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.DespawnCouple.SeqEvent_RemoteEvent_0',
            ],
            're_nousemoxxie': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_17',
            ],
            're_nowmixitup': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_1',
            ],
            're_openvandoor': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.VanDoorInteraction.SeqEvent_RemoteEvent_1',
            ],
            're_pausestomping': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_3',
            ],
            're_playerinrange': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_10',
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_14',
            ],
            're_playertakesbaby': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.SeqEvent_RemoteEvent_2',
            ],
            're_playertakesbackbaby': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_10',
            ],
            're_playertakeswhiskey': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.WhiskeyDrinking.SeqEvent_RemoteEvent_10',
            ],
            're_playertriedwhiskey': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.WhiskeyDrinking.SeqEvent_RemoteEvent_3',
            ],
            're_playersnotinrange': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_15',
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_2',
            ],
            're_preprobotsforopen': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.CoupleGreetsAndDespawns.SeqEvent_RemoteEvent_1',
            ],
            're_releaseintrozafords': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_14',
            ],
            're_removeallwaypoints': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.WhiskeyDrinking.SeqEvent_RemoteEvent_2',
            ],
            're_removetempwaypointfromjunkbot': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_5',
            ],
            're_removewaypointfrombaby': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_9',
            ],
            're_removewaypointfromvat': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_7',
            ],
            're_returndialogresponse': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_ringbellmatinee': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_sendloadertodoor': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.CoupleGreetsAndDespawns.SeqEvent_RemoteEvent_3',
            ],
            're_sendtodespawncouple': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.SeqEvent_RemoteEvent_3',
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.ThresherCombat.SeqEvent_RemoteEvent_1',
            ],
            're_setupcrashmoment': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.SeqEvent_RemoteEvent_2',
            ],
            're_showmissionpickup': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.WhiskeyDrinking.SeqEvent_RemoteEvent_6',
            ],
            're_spawnbot': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.RobotSetupSequences.SeqEvent_RemoteEvent_12',
            ],
            're_spawnmoxxieintro': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_5',
            ],
            're_spawnnate': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_spawnstellabot_onload': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_4',
            ],
            're_spawnzafordguys': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_13',
            ],
            're_startmoxxiewalktodoor': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.SeqEvent_RemoteEvent_1',
            ],
            're_stopbellringingmatinee': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_stopbotmovingtowardwall': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_24',
            ],
            're_stoppolemovement': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.MainFishingSequence.SeqEvent_RemoteEvent_0',
            ],
            're_takeoff': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_talkedtorobot': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_11',
            ],
            're_talkedtorobotagain': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_12',
            ],
            're_teleportmoxxietochurch': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.SeqEvent_RemoteEvent_8',
            ],
            're_testbaby': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_12',
            ],
            're_triggerplayercamebackdialog': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_6',
            ],
            're_triggerplayerleftdialog': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_7',
            ],
            're_turnoffbadasstrig': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_3',
            ],
            're_turnoffdrizzleaudio': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_turnoffpourbutton': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_5',
            ],
            're_turnofftownperches': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.KillHodunksCombat.SeqEvent_RemoteEvent_10',
            ],
            're_turnoffvatbutton': [
                'Distillery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_2',
            ],
            're_turnoffweather': [
                'DISTILLERY_LIGHT2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_turnoffweatherbehaviorvolumes': [
                'Distillery_Skybox.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_turnonmoxxieusability': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_20',
            ],
            're_turnonpourbutton': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_4',
            ],
            're_turnonvatbutton': [
                'Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence.LovePotionSequence.SeqEvent_RemoteEvent_6',
            ],
            're_turnonweatherbehaviorvolumes': [
                'Distillery_Skybox.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_unhidemoxxiejunkloader': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_0',
            ],
            're_unhidemoxxiespeaker': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_2',
            ],
            're_updatescriptedmove': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_1',
            ],
            're_usemoxxie': [
                'Distillery_IntroOutro.TheWorld:PersistentLevel.Main_Sequence.MoxxieSequences.Moxxie_Spawning.SeqEvent_RemoteEvent_18',
            ],
            're_vandoorglow_off': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.HodunkTownSequences.VanDoorInteraction.SeqEvent_RemoteEvent_0',
            ],
            're_fishingpole_unusable': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.SeqEvent_RemoteEvent_6',
            ],
            're_groomsmenfight_go': [
                'Distillery_Mission2.TheWorld:PersistentLevel.Main_Sequence.DistilleryCombat.SeqEvent_RemoteEvent_9',
            ],
            're_internal_pingretreatroutine': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_21',
            ],
            're_internal_playersinrange': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_0',
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_17',
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_18',
            ],
            're_internal_playersnotinrange': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_20',
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.FollowRobotMissionControl.SeqEvent_RemoteEvent_22',
            ],
            're_makeglow': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.BaitControl.SeqEvent_RemoteEvent_0',
            ],
            're_makepolesusable': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.SeqEvent_RemoteEvent_7',
            ],
            're_resetthreshers': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.ThresherCombat.SeqEvent_RemoteEvent_0',
            ],
            're_resettownonreturn': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.ReturnToWedding.SeqEvent_RemoteEvent_0',
            ],
            're_reverseline': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.MainFishingSequence.SeqEvent_RemoteEvent_9',
            ],
            're_spawnhodunkwatershooter': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.ThresherCombat.SeqEvent_RemoteEvent_4',
            ],
            're_stelladead': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_thresherbaitpickupup': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.BaitControl.SeqEvent_RemoteEvent_24',
            ],
            're_thresherbaitpickupup_1': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.BaitControl.SeqEvent_RemoteEvent_41',
            ],
            're_thresherbaitpickupup_2': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.BaitControl.SeqEvent_RemoteEvent_38',
            ],
            're_thresherbaitpickupup_3': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.BaitControl.SeqEvent_RemoteEvent_39',
            ],
            're_thresherbaitpickupup_4': [
                'Distillery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Fishing.BaitControl.SeqEvent_RemoteEvent_40',
            ],
            're_turnoffstellawaypoint': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_turnoffstellawaypoint_2': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_turnonstellawaypoint_2': [
                'Distillery_Side_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_walkingcombatdone': [
                'Distillery_Mission.TheWorld:PersistentLevel.Main_Sequence.BotGateGuardSequences.SeqEvent_RemoteEvent_9',
            ],
        },
        'orchid_shipgraveyard_p': {
            'm7_explodehermit': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'orchid_m5_trigherbertintro': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'orchid_m5_turnin': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'orchid_m6_chestopened': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'orchid_m6_kickoff': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'orchid_m6_returntoherbert': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'orchid_m7_explodeherbert': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'orchid_m7_fixcompass': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'orchid_m7_kickoff': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'orchid_m7_returntoherbert': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'orchid_m7_takecompass': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'setleverglowon': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'debughermit': [
                'Orchid_ShipGraveyard_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
        },
        'sanctuaryair_p': {
            'accusedbarlo': [
                'SanctuaryAir_Side.TheWorld:PersistentLevel.Main_Sequence.WontGetFooled.SeqEvent_RemoteEvent_0',
            ],
            'brickgetup': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode12.SeqEvent_RemoteEvent_1',
            ],
            'brickoffperch': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_5',
            ],
            'claptrapbeatbox': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClapTrap.SeqEvent_RemoteEvent_1',
            ],
            'claptrapstartpatrol': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClapTrap.SeqEvent_RemoteEvent_0',
            ],
            'claptrapstashtalkanim': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClapTraps_SecretStash.SeqEvent_RemoteEvent_0',
            ],
            'echohyperion': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.script_AngelRolandLilithConversation.SeqEvent_RemoteEvent_1',
            ],
            'ennispatrol': [
                'SanctuaryAir_Side.TheWorld:PersistentLevel.Main_Sequence.WontGetFooled.SeqEvent_RemoteEvent_4',
            ],
            'ep10_claptrapupgradeanim': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_5',
            ],
            'ep11_conversationfinished': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode11.SeqEvent_RemoteEvent_4',
            ],
            'ep3_shieldup': [
                'SanctuaryAir_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'ep4_enabledens': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'ep7_disabledens': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'ep7_enablepanicdens': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'ep8_disablepanicden': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ep8_enabledens': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'getintopositionfor13kickoff': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_7',
            ],
            'givebadtouch': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Moxxi.SeqEvent_RemoteEvent_2',
            ],
            'givegoodtouch': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Moxxi.SeqEvent_RemoteEvent_0',
            ],
            'harkpatrol': [
                'SanctuaryAir_Side.TheWorld:PersistentLevel.Main_Sequence.WontGetFooled.SeqEvent_RemoteEvent_6',
            ],
            'hidefavor': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClapTrapBirthdayBash.SeqEvent_RemoteEvent_0',
            ],
            'kickoffcomplete': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_3',
            ],
            'lilithapproach': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode11.SeqEvent_RemoteEvent_0',
            ],
            'lilithoffperch': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_4',
            ],
            'marcuspatrolaftersmashandgrab': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Marcus.SeqEvent_RemoteEvent_1',
            ],
            'marcusstartpatrol': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Marcus.SeqEvent_RemoteEvent_0',
            ],
            'mordecaigetoffperch': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode12.SeqEvent_RemoteEvent_2',
            ],
            'mordecaileave': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.BloodwingConversation.SeqEvent_RemoteEvent_0',
            ],
            'mordecaioffperch': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_6',
            ],
            'mordylookdown': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BrickMordyConversations.SeqEvent_RemoteEvent_0',
            ],
            'musiconload': [
                'SanctuaryAir_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'npc_patrol': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'npcs run in fear': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'ontakedamage': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'poeticlicense_timetodie': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PoeticLicense.SeqEvent_RemoteEvent_2',
            ],
            're_ep14_closemarcusdoor': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_2',
            ],
            're_ep14_openmarcusdoor': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_3',
            ],
            're_starttannispatrol': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Tannis.SeqEvent_RemoteEvent_0',
            ],
            're_tv_rolandhq_ep10_pauseimage2': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.script_AngelRolandLilithConversation.BinkControl.SeqEvent_RemoteEvent_8',
            ],
            're_tv_rolandhq_ep10_pauseimage3': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.script_AngelRolandLilithConversation.BinkControl.SeqEvent_RemoteEvent_7',
            ],
            're_tv_rolandhq_ep10_pauseimage4': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.script_AngelRolandLilithConversation.BinkControl.SeqEvent_RemoteEvent_6',
            ],
            're_tv_rolandhq_ep10_showangelgoodbye': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.script_AngelRolandLilithConversation.BinkControl.SeqEvent_RemoteEvent_9',
            ],
            're_tv_rolandhq_ep10_showangelstart': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.script_AngelRolandLilithConversation.SeqEvent_RemoteEvent_3',
            ],
            're_tv_rolandhq_ep10_showimage2': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.script_AngelRolandLilithConversation.BinkControl.SeqEvent_RemoteEvent_2',
            ],
            're_tv_rolandhq_ep10_showimage3': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.script_AngelRolandLilithConversation.BinkControl.SeqEvent_RemoteEvent_4',
            ],
            're_tv_rolandhq_ep10_showimage4': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.script_AngelRolandLilithConversation.BinkControl.SeqEvent_RemoteEvent_5',
            ],
            'rm_bearerbadnews_openarmory': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BearerOfBadNews.SeqEvent_RemoteEvent_0',
            ],
            'respawnpawn': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'restartpatrolsminusmordecai': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'returntopost': [
                'SanctuaryAir_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'rockspaper_movetargetforward': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_5',
            ],
            'rockspaper_sendtargetback': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_6',
            ],
            'rockspaper_targetkilled_reset': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_1',
            ],
            'scootergarage': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Scooters_Garage.SeqEvent_RemoteEvent_1',
            ],
            'shinpatrol': [
                'SanctuaryAir_Side.TheWorld:PersistentLevel.Main_Sequence.WontGetFooled.SeqEvent_RemoteEvent_5',
            ],
            'slaphappy_putarmon': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SlapHappy.SeqEvent_RemoteEvent_0',
            ],
            'spawntargetdummy': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TargetDummy.SeqEvent_RemoteEvent_2',
            ],
            'startallvaulthunterpatrols': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'startbrickpatrol': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'startlilithpatrol': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'startmordecaipatrol': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'startmoxxipatrol': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Moxxi.SeqEvent_RemoteEvent_3',
            ],
            'startpartymusic': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClapTrapBirthdayBash.SeqEvent_RemoteEvent_1',
            ],
            'startprojector': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_0',
            ],
            'startrolandpatrol': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'stopmarshallmoving': [
                'SanctuaryAir_Side.TheWorld:PersistentLevel.Main_Sequence.WontGetFooled.SeqEvent_RemoteEvent_1',
                'SanctuaryAir_Side.TheWorld:PersistentLevel.Main_Sequence.WontGetFooled.SeqEvent_RemoteEvent_2',
            ],
            'stopmovingclaptrap': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'teleportmarshall': [
                'SanctuaryAir_Side.TheWorld:PersistentLevel.Main_Sequence.WontGetFooled.SeqEvent_RemoteEvent_3',
            ],
            'zedstartpatrol': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DrZed.SeqEvent_RemoteEvent_0',
            ],
            'debugmarcus': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Marcus.SeqEvent_RemoteEvent_12',
            ],
            'debugtannis': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Tannis.SeqEvent_RemoteEvent_6',
            ],
            'debugzed': [
                'SanctuaryAir_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DrZed.SeqEvent_RemoteEvent_7',
            ],
            're_wgfa_diableusability': [
                'SanctuaryAir_Side.TheWorld:PersistentLevel.Main_Sequence.WontGetFooled.SeqEvent_RemoteEvent_9',
            ],
        },
        'sanctuary_p': {
            'angeloff': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_19',
            ],
            'angelonscreen': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_18',
            ],
            'animplayer_teleporthands': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_3',
            ],
            'blockall': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_44',
            ],
            'blockweapons': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_43',
            ],
            'claptrapbeatbox': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClapTrap.SeqEvent_RemoteEvent_1',
            ],
            'claptrapstartpatrol': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClapTrap.SeqEvent_RemoteEvent_2',
            ],
            'claptrapstashtalkanim': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ClapTraps_SecretStash.SeqEvent_RemoteEvent_5',
            ],
            'closegate': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_11',
            ],
            'debugpillar': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_0',
            ],
            'debugsanctuaryliftoff': [
                'Sanctuary_Outer.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'debugshieldcharge': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_16',
            ],
            'debugshieldfailure': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_10',
            ],
            'disable_beams': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_24',
            ],
            'enable_beams': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_25',
            ],
            'end_force_move': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_41',
            ],
            'ep3_beginhyperionattack': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_1',
            ],
            'ep3_shieldup': [
                'Sanctuary_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_9',
            ],
            'ep4_enabledens': [
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'ep4_opensanctuarygate': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_10',
            ],
            'ep4_plugincoresparks': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_14',
            ],
            'ep4_returntopost': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_11',
            ],
            'ep4_sparks': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_13',
            ],
            'ep7_disabledens': [
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'ep7_enablepanicdens': [
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'ep8activeload': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_17',
            ],
            'ep8_disablepanicden': [
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ep8_enabledens': [
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'ep8_gateopen': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_12',
            ],
            'episode8_removedoldcore': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_7',
            ],
            'facedirection': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_39',
            ],
            'gibevent1': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_22',
            ],
            'gibevent2': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_31',
            ],
            'gibevent3': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_34',
            ],
            'givebadtouch': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Moxxi.SeqEvent_RemoteEvent_2',
            ],
            'givegoodtouch': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Moxxi.SeqEvent_RemoteEvent_0',
            ],
            'guard1runs': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_36',
            ],
            'level loaded': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_12',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_13',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_14',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_15',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_2',
            ],
            'marcuspatrolaftersmashandgrab': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Marcus.SeqEvent_RemoteEvent_1',
            ],
            'marcusstartpatrol': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Marcus.SeqEvent_RemoteEvent_0',
            ],
            'musiconload': [
                'Sanctuary_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'npc_patrol': [
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'npcs run in fear': [
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'onactiveloadgiveeridium': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_16',
            ],
            'opensanctuarygate': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_3.SeqEvent_RemoteEvent_0',
            ],
            'pathstart': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Scooters_Garage.SeqEvent_RemoteEvent_0',
            ],
            'playtitlecard': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_3',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Scooters_Garage.SeqEvent_RemoteEvent_3',
            ],
            'play_powerup_anim': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_6',
            ],
            'poeticlicense_timetodie': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PoeticLicense.SeqEvent_RemoteEvent_0',
            ],
            'puthanddown': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_38',
            ],
            're_backgroundsanctuarybombardment': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_23',
            ],
            're_ep14_closemarcusdoor': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_2',
            ],
            're_ep14_openmarcusdoor': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_3',
            ],
            're_ep3sanctuarybombardment': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_27',
            ],
            're_playsiren': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_7',
            ],
            're_startbombardment': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_22',
            ],
            're_startscootertitlecard': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_0',
            ],
            're_stopbombardment': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_1',
            ],
            're_trytoremovecore': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_1',
            ],
            're_stopsiren': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_8',
            ],
            'rf_gets_pwned': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_26',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_28',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_30',
            ],
            'randommoonshotattack': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_21',
            ],
            're_startset2': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_4',
            ],
            're_startset3': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_5',
            ],
            're_startset4': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_6',
            ],
            're_startset5': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_2',
            ],
            'reset delay': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_15',
            ],
            'respawnpawn': [
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'returntopost': [
                'Sanctuary_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_23',
            ],
            'rockspaper_movetargetforward': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_5',
            ],
            'rockspaper_sendtargetback': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_6',
            ],
            'rockspaper_targetkilled_reset': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RocksPaperGenocide.SeqEvent_RemoteEvent_1',
            ],
            'scootergarage': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Scooters_Garage.SeqEvent_RemoteEvent_1',
            ],
            'scootertocenteroftown': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_20',
            ],
            'setgaragelastframe': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Scooters_Garage.SeqEvent_RemoteEvent_2',
            ],
            'shieldimpactleft': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_17',
            ],
            'shieldimpactright': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_18',
            ],
            'shieldimpacttop': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_11',
            ],
            'shield_offline': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_29',
            ],
            'sparks': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_40',
            ],
            'spawntargetdummy': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TargetDummy.SeqEvent_RemoteEvent_2',
            ],
            'spleen': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_2',
            ],
            'startallvaulthunterpatrols': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'startbrickpatrol': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'startep8set1': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_3',
            ],
            'startep8set2': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_12',
            ],
            'startep8set3': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_19',
            ],
            'startep8set4': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_20',
            ],
            'startep8set5': [
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_36',
            ],
            'startlilithfx': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_37',
            ],
            'startlilithpatrol': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'startmordecaipatrol': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'startmoxxipatrol': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Moxxi.SeqEvent_RemoteEvent_1',
            ],
            'startrolandpatrol': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'start_force_move': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_4',
            ],
            'stoplilithfx': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_32',
            ],
            'teleportinstart': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_11',
            ],
            'teleportlilithout': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_8',
            ],
            'teleporttocenter': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_9',
            ],
            'togglebridge': [
                'Sanctuary_Land.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'triggerms1': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_24',
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_26',
            ],
            'triggerms2': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_25',
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_28',
            ],
            'triggerms3': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_27',
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_30',
            ],
            'triggerms4': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_29',
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_32',
            ],
            'triggerms5': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_33',
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_35',
            ],
            'triggerms6': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_35',
                'Sanctuary_FX.TheWorld:PersistentLevel.Main_Sequence.ShieldAndMoonshotScripting.SeqEvent_RemoteEvent_33',
            ],
            'waitingforeridium': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_8.SeqEvent_RemoteEvent_10',
            ],
            'walk': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_4',
            ],
            'zedstartpatrol': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DrZed.SeqEvent_RemoteEvent_0',
            ],
            'audio_screams_load': [
                'Sanctuary_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'debugmarcus': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_12',
            ],
            'debugscooter': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_5',
            ],
            'debugtannis': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_6',
            ],
            'debugzed': [
                'Sanctuary_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode_4.SeqEvent_RemoteEvent_7',
            ],
        },
        'sanctuary_hole_p': {
            'poweron': [
                'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.SeqEvent_RemoteEvent_0',
                'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.SeqEvent_RemoteEvent_1',
            ],
            're_safeandsoundbandits': [
                'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'gotime': [
                'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'onnow': [
                'Sanctuary_Hole_P.TheWorld:PersistentLevel.Main_Sequence.Scripting.SeqEvent_RemoteEvent_2',
            ],
        },
        'craterlake_p': {
            'are_animationstart': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Ulysess.SeqEvent_RemoteEvent_2',
            ],
            'are_moveulysess': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Ulysess.SeqEvent_RemoteEvent_3',
            ],
            'are_turnontriggervolume': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Ulysess.SeqEvent_RemoteEvent_0',
            ],
            'are_ulyssessavestate': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Ulysess.SeqEvent_RemoteEvent_1',
            ],
            'closeelevatordoor': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'eastereggstart': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.FUN.SeqEvent_RemoteEvent_0',
            ],
            'ep16_spawnslabgyroa': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode16.SeqEvent_RemoteEvent_1',
            ],
            'ep16_spawnslabgyrob': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode16.SeqEvent_RemoteEvent_2',
            ],
            'ep16_spawnslabgyroc': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode16.SeqEvent_RemoteEvent_3',
            ],
            'ep16_spawnslabgyrod': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode16.SeqEvent_RemoteEvent_0',
            ],
            'openelevatordoor': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_activateep16mortarden': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode16.SeqEvent_RemoteEvent_8',
            ],
            're_capflags_allowflag1up': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_13',
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_2',
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Capture_The_Flags.SeqEvent_RemoteEvent_2',
            ],
            're_capflags_allowflag2up': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_14',
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_5',
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Capture_The_Flags.SeqEvent_RemoteEvent_5',
            ],
            're_capflags_allowflag3up': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_7',
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_9',
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Capture_The_Flags.SeqEvent_RemoteEvent_1',
            ],
            're_capflags_stopflag1up': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_3',
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Capture_The_Flags.SeqEvent_RemoteEvent_3',
            ],
            're_capflags_stopflag2up': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_4',
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Capture_The_Flags.SeqEvent_RemoteEvent_4',
            ],
            're_capflags_stopflag3up': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_8',
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Capture_The_Flags.SeqEvent_RemoteEvent_0',
            ],
            're_whoisontheelevator_bottom': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_whoisontheelevator_top': [
                'CraterLake_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'rm_captureflag1done': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_6',
            ],
            'rm_captureflag2done': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_11',
            ],
            'rm_captureflag3done': [
                'CraterLake_Combat.TheWorld:PersistentLevel.Main_Sequence.CaptureTheFlags.SeqEvent_RemoteEvent_10',
            ],
            'rm_moonorbitlaunch': [
                'CraterLake_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
        },
        'sage_rockforest_p': {
            'challenge_bewaretheclap_sacrifice': [
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'challenge_rakkforest_nestdestroyed': [
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'claptrap_panic': [
                'Sage_RockForest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'claptrap_throne': [
                'Sage_RockForest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'dahliamurder_gunfired': [
                'Sage_RockForest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'enablerockforesttosubstation': [
                'Sage_RockForest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'm3_trigsaveclaptrap': [
                'Sage_RockForest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'notsofriendly_destroyvillage1': [
                'Sage_RockForest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'notsofriendly_destroyvillage2': [
                'Sage_RockForest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'sm_followglow_active': [
                'Sage_RockForest_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'sm_oldpukey_disableattackers': [
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'sm_pukey_activatepukeyden': [
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'sm_urine_missionactive': [
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'sm_urine_triggercombat': [
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'sage_follow_decal_all_hide': [
                'Sage_RockForest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'sage_follow_decal_all_show': [
                'Sage_RockForest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'sage_urine_decal_01_hide': [
                'Sage_RockForest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'sage_urine_decal_02_hide': [
                'Sage_RockForest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'sage_urine_decal_03_hide': [
                'Sage_RockForest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'sage_urine_decal_04_hide': [
                'Sage_RockForest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'sage_urine_decal_05_hide': [
                'Sage_RockForest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'sage_urine_decal_all_hide': [
                'Sage_RockForest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'sage_urine_decal_all_show': [
                'Sage_RockForest_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'sunrise': [
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'sunset': [
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Sage_RockForest_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
        },
        'iris_hub2_p': {
            'debugmamma': [
                'Iris_Hub2_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'disablesupportbikers': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_54',
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_76',
            ],
            'dustdevils': [
                'Iris_Hub2_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'enablesupportbikers': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_55',
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_75',
            ],
            'endmotormommawanderforidiotplayer': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'enoughsupportbikerskilled': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'iris_hub_resetraidsupportbikes': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'iris_interviewcompleted': [
                'Iris_Hub2_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'iris_matteroftaste_pass1off': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            'iris_matteroftaste_pass1on': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'iris_matteroftaste_pass2off': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'iris_matteroftaste_pass2on': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'iris_updatetheboard': [
                'Iris_Hub2_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'manualsandstorm': [
                'Iris_Hub2_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'motormamabikehealthbaroff': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'motormamabiketurrets01killed': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_69',
            ],
            'motormamabiketurrets02killed': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
            ],
            'motormamabiketurrets03killed': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_73',
            ],
            'motormamaenteringpatrol': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'motormamagettinginjured': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            'motormamahealthbaroff': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            'motormamaspawneron': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_startcrush_titlecard': [
                'Iris_Hub2_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_startingrabposition': [
                'Iris_Hub2_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'raidphase2levelone': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'raidphase2levelthree': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_57',
            ],
            'raidphase2leveltwo': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            'ring01supportbiker01': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_74',
            ],
            'ring01supportbiker02': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'ring01supportbiker03': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'ring01supportbiker04': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'ring02supportbiker01': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'ring02supportbiker02': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'ring02supportbiker03': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'ring02supportbiker04': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'ring03supportbiker01': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'ring03supportbiker02': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'ring03supportbiker03': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'ring03supportbiker04': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'ring04supportbiker01': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_56',
            ],
            'ring04supportbiker02': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            'ring04supportbiker03': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_44',
            ],
            'ring04supportbiker04': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_45',
            ],
            'ring05supportbiker01': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
            ],
            'ring05supportbiker02': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_49',
            ],
            'ring05supportbiker03': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_48',
            ],
            'ring05supportbiker04': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_50',
            ],
            'ring06supportbiker01': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_67',
            ],
            'ring06supportbiker02': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_53',
            ],
            'ring06supportbiker03': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_47',
            ],
            'ring06supportbiker04': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_52',
            ],
            'ring07supportbiker01': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ring07supportbiker02': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_58',
            ],
            'ring07supportbiker03': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_60',
            ],
            'ring07supportbiker04': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_63',
            ],
            'ring08supportbiker01': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_61',
            ],
            'ring08supportbiker02': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_66',
            ],
            'ring08supportbiker03': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_59',
            ],
            'ring08supportbiker04': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_64',
            ],
            'ring09supportbiker01': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_65',
            ],
            'ring09supportbiker02': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
            ],
            'ring09supportbiker03': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_62',
            ],
            'ring09supportbiker04': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_51',
            ],
            'sandstorm': [
                'Iris_Hub2_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'startmotormommawanderforidiotplayer': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'supportbikerkilled': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'supportbikerspawned': [
                'Iris_Hub2_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_titlecard_hidestuff': [
                'Iris_Hub2_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
        },
        'cove_p': {
            'activate_elevator_audio': [
                'Cove_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'closefiredoor': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'ep2c_openbackflyntdoor': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'flintcommand': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FlyntFireAttack.SeqEvent_RemoteEvent_0',
            ],
            'flynt_spawnfirepsychos': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FlyntFireAttack.SeqEvent_RemoteEvent_1',
            ],
            'glacial_activatedragonfire': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FlyntFireAttack.SeqEvent_RemoteEvent_4',
            ],
            'handsomejackhere_opencontainerdoor': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HandsomeJackHere.SeqEvent_RemoteEvent_1',
            ],
            'handsomejackhere_opentrashdoor': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HandsomeJackHere.SeqEvent_RemoteEvent_0',
            ],
            'handsomejackhere_trashdoorglowon': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HandsomeJackHere.SeqEvent_RemoteEvent_2',
            ],
            'openfiredoor': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'resetgallows': [
                'Cove_LiarsBerg.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'resetlower': [
                'Cove_LiarsBerg.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'turnofffence_1': [
                'Cove_P.TheWorld:PersistentLevel.Main_Sequence.ElectricalFence.SeqEvent_RemoteEvent_4',
            ],
            'warmongroared': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Symbiosis.SeqEvent_RemoteEvent_0',
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Symbiosis.SeqEvent_RemoteEvent_1',
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Symbiosis.SeqEvent_RemoteEvent_2',
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Symbiosis.SeqEvent_RemoteEvent_3',
            ],
            'debugboomboom': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'debugflynt': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'debughammerlock': [
                'Cove_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
        },
        'southernshelf_p': {
            'activate_elevator_audio': [
                'SouthernShelf_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'big_dismountcannon': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'boomboom_ground2': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'closefiredoor': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'dropdown': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'ep2c_openbackflyntdoor': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'flintcommand': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FlyntFireAttack.SeqEvent_RemoteEvent_0',
            ],
            'flynt_spawnfirepsychos': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FlyntFireAttack.SeqEvent_RemoteEvent_1',
            ],
            'generator_button_audio': [
                'SouthernShelf_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'glacial_activatedragonfire': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FlyntFireAttack.SeqEvent_RemoteEvent_4',
            ],
            'handsomejackhere_opencontainerdoor': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HandsomeJackHere.SeqEvent_RemoteEvent_1',
            ],
            'handsomejackhere_opentrashdoor': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HandsomeJackHere.SeqEvent_RemoteEvent_0',
            ],
            'handsomejackhere_trashdoorglowon': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.HandsomeJackHere.SeqEvent_RemoteEvent_2',
            ],
            'little_dismountcannon': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'movetogate': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'openfiredoor': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'playfleshripperlines': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.GATE_SEQUENCE.SeqEvent_RemoteEvent_0',
            ],
            'playercrossed': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'playerdamagedbycannon': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.CannonChallenge.SeqEvent_RemoteEvent_6',
            ],
            'playerincannon': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'playerleftcannon': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'playertouchedburningplate': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FlyntFireAttack.SeqEvent_RemoteEvent_5',
            ],
            'resetgallows': [
                'SouthernShelf_LiarsBerg.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'resetlower': [
                'SouthernShelf_LiarsBerg.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'turnfenceon': [
                'SouthernShelf_P.TheWorld:PersistentLevel.Main_Sequence.ElectricalFence.SeqEvent_RemoteEvent_0',
            ],
            'turnofffence_1': [
                'SouthernShelf_P.TheWorld:PersistentLevel.Main_Sequence.ElectricalFence.SeqEvent_RemoteEvent_4',
            ],
            'debugboomboom': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'debugflynt': [
                'SouthernShelf_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
        },
        'southpawfactory_p': {
            'asstheass_openexitdoor': [
                'SouthpawFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'closeintrogate': [
                'SouthpawFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Assassin1.SeqEvent_RemoteEvent_1',
            ],
            'opengate2': [
                'SouthpawFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Assassin2.SeqEvent_RemoteEvent_3',
            ],
            'opengate3': [
                'SouthpawFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Assassin3.SeqEvent_RemoteEvent_2',
            ],
            'spawn assassin4': [
                'SouthpawFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.assassin4.SeqEvent_RemoteEvent_4',
            ],
        },
        'thresherraid_p': {
            'resetself': [
                'ThresherRaid_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'summonthresher': [
                'ThresherRaid_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'ThresherRaid_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
        },
        'grass_cliffs_p': {
            'cliffsactivatedoor1constructor': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_5',
            ],
            'cliffsactivatefactorydoor': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode11.SeqEvent_RemoteEvent_1',
            ],
            'cliffsactivatehyperiondoor1': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_4',
            ],
            'cliffsactivatehyperiondoor2': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_3',
            ],
            'cliffsactivatehyperiondoor3': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_1',
            ],
            'cliffsactivatepillbox1': [
                'Grass_Cliffs_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'cliffsdropcargocontainer': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'poeticlicense_swapbanditmaterial': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PoeticLicense.SeqEvent_RemoteEvent_0',
            ],
            're_beacon01destroyed': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_1',
            ],
            're_beacon02destroyed': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_2',
            ],
            're_beacon03destroyed': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_0',
            ],
            're_brickatdoor': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode11.SeqEvent_RemoteEvent_2',
            ],
            're_claptrapdeactivatesbarrier': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode13.SeqEvent_RemoteEvent_0',
            ],
            're_ep11_brickragevo': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_43',
            ],
            're_ep11_disablebotchatter': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_28',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_34',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_37',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_42',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_46',
            ],
            're_ep11_disablerandompraise': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_14',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_15',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_24',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_31',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_4',
            ],
            're_ep11_elementaldeath': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_26',
            ],
            're_ep11_enablebotchatter': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_27',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_35',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_38',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_41',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_45',
            ],
            're_ep11_enablerandompraise': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_12',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_16',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_23',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_25',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_7',
            ],
            're_ep11_factorybattle_playerkill': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_32',
            ],
            're_ep11_factorybattle_playersecondwind': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_5',
            ],
            're_ep11_gibdeath': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_6',
            ],
            're_ep11_goliathpowerup': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_17',
            ],
            're_ep11_mortarbattle_brickkill': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_39',
            ],
            're_ep11_mortarbattle_playerdown': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_36',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_40',
            ],
            're_ep11_mortarbattle_playerkill': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_33',
            ],
            're_ep11_mortarwarning': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_49',
            ],
            're_ep11_playerleftreaction': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_48',
            ],
            're_ep11_regulardeath': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_10',
            ],
            're_ep11_releasethehounds': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_19',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_21',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_22',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_52',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_53',
            ],
            're_ep11_shoottheshield': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_47',
            ],
            're_lowerbarricadefailsafe': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_moonshotbeacon01': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_50',
            ],
            're_moonshotbeacon02': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_51',
            ],
            're_moonshotbeacon03': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_44',
            ],
            're_openfactorydoor': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode11.SeqEvent_RemoteEvent_6',
            ],
            're_pickabrickperch': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_13',
            ],
            're_spawncombatbrick': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_29',
            ],
            're_startrobotassault': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_30',
            ],
            're_superpunchimpact': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_11',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_8',
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_9',
            ],
            'shootmeinface_turnonshootlinetrigger': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ShootMeInTheFace.SeqEvent_RemoteEvent_0',
            ],
            'slabtower_beacon1goliathlocked': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.DefendSlabTower_SideMission.SeqEvent_RemoteEvent_9',
            ],
            'slabtower_beacon1marauderlocked': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.DefendSlabTower_SideMission.SeqEvent_RemoteEvent_8',
            ],
            'slabtower_beacon1psycholocked': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.DefendSlabTower_SideMission.SeqEvent_RemoteEvent_3',
            ],
            'slabtower_beacon2goliathlocked': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.DefendSlabTower_SideMission.SeqEvent_RemoteEvent_10',
            ],
            'slabtower_beacon2marauderlocked': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.DefendSlabTower_SideMission.SeqEvent_RemoteEvent_7',
            ],
            'slabtower_beacon2psycholocked': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.DefendSlabTower_SideMission.SeqEvent_RemoteEvent_4',
            ],
            'slabtower_beacon3goliathlocked': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.DefendSlabTower_SideMission.SeqEvent_RemoteEvent_13',
            ],
            'slabtower_beacon3marauderlocked': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.DefendSlabTower_SideMission.SeqEvent_RemoteEvent_11',
            ],
            'slabtower_beacon3psycholocked': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.DefendSlabTower_SideMission.SeqEvent_RemoteEvent_0',
            ],
            'thresherraid_openthresherdoors': [
                'Grass_Cliffs_P.TheWorld:PersistentLevel.Main_Sequence.ThresherRaid.SeqEvent_RemoteEvent_1',
            ],
            'thresherraid_pedestalused': [
                'Grass_Cliffs_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThresherRaid.SeqEvent_RemoteEvent_0',
            ],
            'debugbrick': [
                'Grass_Cliffs_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode11_Combat.SeqEvent_RemoteEvent_3',
            ],
        },
        'ice_p': {
            'ep3_netmoduletaken': [
                'Ice_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'ep3_opensanctuarygate': [
                'Ice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode03.SeqEvent_RemoteEvent_0',
            ],
            'ep3_opensanctuarygatelastframe': [
                'Ice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode03.SeqEvent_RemoteEvent_2',
            ],
            're_activatedeaddroptriggers': [
                'Ice_P.TheWorld:PersistentLevel.Main_Sequence.HiddenDeadDrop.SeqEvent_RemoteEvent_1',
            ],
            're_dropanchor': [
                'Ice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DeadDropAnchor.SeqEvent_RemoteEvent_2',
            ],
            're_ep3_playvanowena': [
                'Ice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode03.SeqEvent_RemoteEvent_4',
            ],
            're_ep3_playvanowenb': [
                'Ice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode03.SeqEvent_RemoteEvent_5',
            ],
            're_ep3_playvanowenc': [
                'Ice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode03.SeqEvent_RemoteEvent_3',
            ],
            're_fallinglight_audio': [
                'Ice_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_snowskaghurt': [
                'Ice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_0',
            ],
            're_spawndoor1': [
                'Ice_P.TheWorld:PersistentLevel.Main_Sequence.SpawnStyleFun.SeqEvent_RemoteEvent_0',
            ],
            're_steamventecho': [
                'Ice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.InMemoriam.SeqEvent_RemoteEvent_1',
            ],
        },
        'frost_p': {
            'bsgate_lowerveryslowly': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_5',
            ],
            'bsgate_pause': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_0',
            ],
            'bsgate_slamshut': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_6',
            ],
            'callforhelp': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_4',
            ],
            'ep3_netmoduletaken': [
                'Frost_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'ep3_opensanctuarygate': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode03.SeqEvent_RemoteEvent_2',
            ],
            'medmystery_spawngunholder': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MedicalMystery.SeqEvent_RemoteEvent_0',
            ],
            'novacancy_droppin': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NoVacancy.SeqEvent_RemoteEvent_2',
            ],
            'novacancy_openpartdoor': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NoVacancy.SeqEvent_RemoteEvent_1',
            ],
            'novacancy_turnonhotelpower': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NoVacancy.SeqEvent_RemoteEvent_5',
            ],
            're_lowerdrawbridge': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodshotSlums.SeqEvent_RemoteEvent_0',
            ],
            're_spawndoor1': [
                'Frost_P.TheWorld:PersistentLevel.Main_Sequence.SpawnStyleFun.SeqEvent_RemoteEvent_0',
            ],
            'rm_anyvehicle_playhorn': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_3',
            ],
            'rm_technicalvehicle_playhorn': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_8',
            ],
            'debugmaw': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodshotSlums.SeqEvent_RemoteEvent_1',
            ],
            'debugramp': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode03.SeqEvent_RemoteEvent_1',
            ],
            're_bsoutergateopeningslowly': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_1',
            ],
            're_badmawspawned': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.BloodshotSlums.SeqEvent_RemoteEvent_2',
            ],
            're_displayhorntip': [
                'Frost_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode6.SeqEvent_RemoteEvent_7',
            ],
        },
        'tundraexpress_p': {
            'are_electirictyoff': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.CordiallyInvited.SeqEvent_RemoteEvent_4',
            ],
            'are_electirictyon': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.CordiallyInvited.SeqEvent_RemoteEvent_2',
            ],
            'are_shockfleshstick': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.CordiallyInvited.SeqEvent_RemoteEvent_1',
            ],
            'ep7_rolandhints_bugmorphkillednormal': [
                'TundraExpress_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode7.SeqEvent_RemoteEvent_0',
            ],
            'hit_detected_factory': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gates.SeqEvent_RemoteEvent_3',
            ],
            'hit_detected_farm': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gates.SeqEvent_RemoteEvent_2',
            ],
            'nohardfeelings_blowopendoor1': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NoHardFeelings.SeqEvent_RemoteEvent_0',
            ],
            'nohardfeelings_blowopendoor2': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NoHardFeelings.SeqEvent_RemoteEvent_1',
            ],
            'nohardfeelings_patrolattacked': [
                'TundraExpress_Combat.TheWorld:PersistentLevel.Main_Sequence.NoHardFeelings.SeqEvent_RemoteEvent_7',
                'TundraExpress_Combat.TheWorld:PersistentLevel.Main_Sequence.NoHardFeelings.SeqEvent_RemoteEvent_8',
            ],
            'nohardfeelings_patroltakesdamage': [
                'TundraExpress_Combat.TheWorld:PersistentLevel.Main_Sequence.NoHardFeelings.SeqEvent_RemoteEvent_3',
            ],
            'nohardfeelings_spawntrapbandits': [
                'TundraExpress_Combat.TheWorld:PersistentLevel.Main_Sequence.NoHardFeelings.SeqEvent_RemoteEvent_2',
            ],
            're_activatefleshstick': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.CordiallyInvited.SeqEvent_RemoteEvent_3',
            ],
            're_activatesafes': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TrainRobbery.SeqEvent_RemoteEvent_2',
            ],
            're_bombdisarmed': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Mines.SeqEvent_RemoteEvent_0',
            ],
            'spawnhit': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.CordiallyInvited.SeqEvent_RemoteEvent_0',
            ],
            'tinytina_snore_off': [
                'TundraExpress_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'tinytina_snore_on': [
                'TundraExpress_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'check': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TinyTinaAndCaveArea.SeqEvent_RemoteEvent_1',
            ],
            'debugmordecai': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.BurningVarkidsAndMordecai.SeqEvent_RemoteEvent_3',
            ],
            'debugtina': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TinyTinaAndCaveArea.SeqEvent_RemoteEvent_3',
            ],
            'lerpcam': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.ExternalRemoteEvents.SeqEvent_RemoteEvent_1',
            ],
            're_droptinagate': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Gates.SeqEvent_RemoteEvent_0',
            ],
            're_ep7_tinagaragedoor_pause': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TinyTinaAndCaveArea.script_GarageControl.SeqEvent_RemoteEvent_0',
            ],
            're_ep7_tinagaragedoor_reverse': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TinyTinaAndCaveArea.script_GarageControl.SeqEvent_RemoteEvent_1',
            ],
            're_firetowerused': [
                'TundraExpress_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode7.SeqEvent_RemoteEvent_1',
            ],
            're_mordecai_startshooting': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MordecaiTowerSniper.UpdateMordecaiAimLocation.SeqEvent_RemoteEvent_1',
            ],
            're_openall': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MordecaiTowerSniper.UpdateMordecaiAimLocation.SeqEvent_RemoteEvent_3',
            ],
            're_shutoffshooting': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MordecaiTowerSniper.UpdateMordecaiAimLocation.SeqEvent_RemoteEvent_2',
            ],
            're_startmakingrockets': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TinyTinaAndCaveArea.SeqEvent_RemoteEvent_5',
            ],
            're_tinadialog_thatsrightbitches': [
                'TundraExpress_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_tinapressesoutsidegaragebutton': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TinyTinaAndCaveArea.TinyTinaControl.SeqEvent_RemoteEvent_2',
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TinyTinaAndCaveArea.TinyTinaControl.SeqEvent_RemoteEvent_3',
            ],
            're_tundraexpress_abortmordecaimove': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MordecaiTowerSniper.UpdateMordecaiAimLocation.SeqEvent_RemoteEvent_4',
            ],
            're_tundraexpress_restartmordecaisniping': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MordecaiTowerSniper.UpdateMordecaiAimLocation.SeqEvent_RemoteEvent_0',
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MordecaiTowerSniper.UpdateMordecaiAimLocation.SeqEvent_RemoteEvent_5',
            ],
            're_turnonrocketcoll': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TinyTinaAndCaveArea.SeqEvent_RemoteEvent_2',
            ],
            're_varkidrecentlykilledbyfire': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.BurningVarkidsAndMordecai.SeqEvent_RemoteEvent_1',
            ],
            're_playrocketdialog': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode07.TinaRocketsAndTrainCrash.SeqEvent_RemoteEvent_0',
            ],
            're_reset': [
                'TundraExpress_Dynamic.TheWorld:PersistentLevel.Main_Sequence.TundraTrain.SeqEvent_RemoteEvent_0',
            ],
        },
        'docks_p': {
            'achieve_swordpullout': [
                'Docks_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'chestcombat': [
                'Docks_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'dragonmusic_on': [
                'Docks_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'event_cycletimeofday': [
                'DOCKS_LIGHT.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Docks_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'postcrump_vo3': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.Crumpets.SeqEvent_RemoteEvent_3',
            ],
            'sis_v05': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordInStoner.SeqEvent_RemoteEvent_3',
            ],
            'sis_v06': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordInStoner.SeqEvent_RemoteEvent_5',
            ],
            'sis_v07': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordInStoner.SeqEvent_RemoteEvent_4',
            ],
            'sis_vo1': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordInStoner.SeqEvent_RemoteEvent_14',
            ],
            'sis_vo2': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordInStoner.SeqEvent_RemoteEvent_15',
            ],
            'sis_vo3': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordInStoner.SeqEvent_RemoteEvent_16',
            ],
            'sis_vo4': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordInStoner.SeqEvent_RemoteEvent_2',
            ],
            'swordinstoner_turnonadds1': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordInStoner.SeqEvent_RemoteEvent_1',
            ],
            'swordinstoner_turnonadds2': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.SwordInStoner.SeqEvent_RemoteEvent_0',
            ],
            're_allowskeletonset1appear': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.SeqEvent_RemoteEvent_6',
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.SeqEvent_RemoteEvent_9',
            ],
            're_allowskeletonset2appear': [
                'Docks_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_docks_sunny_music_start': [
                'Docks_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_helperblast': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.SeqEvent_RemoteEvent_1',
            ],
            're_removeblanks': [
                'Docks_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_setthingsforlatejoiners': [
                'Docks_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_stopdragonmatinee': [
                'Docks_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.SeqEvent_RemoteEvent_2',
            ],
            're_tinavostart': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.SeqEvent_RemoteEvent_4',
            ],
            're_turnofftownden': [
                'Docks_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_turnoffworldchangedialog': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.SeqEvent_RemoteEvent_3',
            ],
            're_turnonboneyhelpers': [
                'Docks_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_turnonboneyjumpnodes': [
                'Docks_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_turnonsunnylatejoiners': [
                'DOCKS_LIGHT.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_turnontownden': [
                'Docks_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_unsetthingsforlatejoiners': [
                'Docks_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_dialog_boneymen': [
                'Docks_Mission.TheWorld:PersistentLevel.Main_Sequence.Mission01.SeqEvent_RemoteEvent_0',
            ],
        },
        'boss_volcano_p': {
            'botphasestart': [
                'Boss_Volcano_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'callloaders': [
                'Boss_Volcano_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'configure_boss_jack_music': [
                'Boss_Volcano_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ep17_startjacktitlecard': [
                'Boss_Volcano_Cutscenes.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'ep17_startwarriortitlecard': [
                'Boss_Volcano_Cutscenes.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'init_jackbrain': [
                'Boss_Volcano_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'lowerlava': [
                'Boss_Volcano_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'pushfog': [
                'Boss_Volcano_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_ep17_callmoonshot_load': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Boss_Volcano_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_ep17_endthis_load': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_ep17_finishjack_load': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Boss_Volcano_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_ep17_jackfight_load': [
                'Boss_Volcano_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_ep17_letlilithkilljack_load': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_ep17_warriorfight_load': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Boss_Volcano_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_eridiumburst': [
                'Boss_Volcano_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_jackrantdone': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_lilithkilljackmatinee': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Boss_Volcano_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_lilithkillsjack': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_moonshotthewarrior': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_startjackfight': [
                'Boss_Volcano_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_startwarriorfight': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_warriorkillvolumes': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'raiselava': [
                'Boss_Volcano_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'releasefog': [
                'Boss_Volcano_Light.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'reset_jackfight': [
                'Boss_Volcano_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'shieldprobedead': [
                'Boss_Volcano_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'spawngaurdian': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'start warrior boss music': [
                'Boss_Volcano_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'startlavajiggle': [
                'Boss_Volcano_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'stop jack boss combat music': [
                'Boss_Volcano_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'stop warrior boss music': [
                'Boss_Volcano_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'test_death': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'warrior_bossbaroff': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'warrior_dead': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'warrior_hearthit': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'warrior_readyfordeath': [
                'Boss_Volcano_Combat_Monster.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'debugending': [
                'Boss_Volcano_Cutscenes.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'debugjack': [
                'Boss_Volcano_Cutscenes.TheWorld:PersistentLevel.Main_Sequence.JackTitleCard.SeqEvent_RemoteEvent_0',
            ],
        },
        'easter_p': {
            'boss_fight_music_off': [
                'Easter_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'boss_fight_music_on': [
                'Easter_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'crawmeraxsummonadds': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'crawmeraxsummonadds_mission': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'mre_stopreminderdialog': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'mre_lowersecondbridge': [
                'Easter_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_30active': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_270.SeqEvent_RemoteEvent_45',
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_45',
            ],
            're_activatemayapistons': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_allowrerunnableboss': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_axtontrap_activate': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_bosselevatorbottomtomid': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_bosselevatormidtobottom': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_bosselevatortoptomid': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_cleartimer': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_crawmeraxintro': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_1160.SeqEvent_RemoteEvent_22',
            ],
            're_crawmeraxtitlecard': [
                'Easter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_crawmeraxtitlecardraid': [
                'Easter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_crawmeraxtitlecardreturn': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            're_crawmeraxtitlecardreturnraid': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_disablebossammo': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            're_disablebossdoor': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_disablebosselevator': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_disablebossexit': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            're_disablebossspawnvolumetesting': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_earlobjfinishfinishdialog': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            're_earlopendoordialog': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_1110.SeqEvent_RemoteEvent_29',
            ],
            're_eggonefound': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_270.SeqEvent_RemoteEvent_0',
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_enablebossammo': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            're_enablebossdoor': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_enablebosselevator': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_enablebossexit': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_enableraiddoor': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_eridiumtriggermissionstatehack': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_exitbosshammerlock': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_findmonolithegg': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_660.SeqEvent_RemoteEvent_17',
            ],
            're_finishpirateobj': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_1100.SeqEvent_RemoteEvent_25',
            ],
            're_firstvarkiddialog': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_310.SeqEvent_RemoteEvent_2',
            ],
            're_firstvarkidexplode': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_390.SeqEvent_RemoteEvent_13',
            ],
            're_hammerlockgreet': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_70.SeqEvent_RemoteEvent_0',
            ],
            're_killbossdialog': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_960.SeqEvent_RemoteEvent_10',
            ],
            're_killbossdialogfinished': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            're_lootspew': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            're_movehammerlockbacktostart': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            're_openearlsdoor': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_47',
            ],
            're_openfireplacedoor': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_opentoiletdoor': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            're_postelevatordialogdone': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_1060.SeqEvent_RemoteEvent_0',
            ],
            're_removefakewaypoint': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_rescuedialog': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_1040.SeqEvent_RemoteEvent_20',
            ],
            're_rescuereminder01': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_1020.SeqEvent_RemoteEvent_17',
            ],
            're_rescuereminder02': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_1030.SeqEvent_RemoteEvent_18',
            ],
            're_saveloadsparkyhack': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_setvarkidwaypoint': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_shortvarkidcombat': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_sidemissionspawn': [
                'Easter_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_spawnbloodhound': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            're_spawnmonolithegg': [
                'Easter_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_spawnsidevarkid': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_startcrawmerax': [
                'Easter_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_startearldialog': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_1060.SeqEvent_RemoteEvent_24',
            ],
            're_startpumpfans': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_startpumps': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_taloncutedialog': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_470.SeqEvent_RemoteEvent_44',
            ],
            're_unleashsparky': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_updateaxtonobj': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_updategaigeobj': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_varkidaggro': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_380.SeqEvent_RemoteEvent_10',
            ],
            're_followvarkid2dialog': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_820.SeqEvent_RemoteEvent_6',
            ],
            're_startparticles': [
                'Easter_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
                'Easter_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
            ],
            're_readyforearl': [
                'Easter_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'summonflyntadds': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'treasureeggs_turnoffeggs': [
                'Easter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'treasuremachine_takesyringe': [
                'Easter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Easter_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'turnoffflyntadds': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_activateentirestation': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            're_activatetntplant': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            're_advancefindeggobjset': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_44',
            ],
            're_advancefollowvarkidobjset': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_advanceinjecteggobjset': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_allowvarkidtoflyaway': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            're_continuevarkidhoundtunnels': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
            ],
            're_craboidsrunaway': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_enablebridgeencountertrigger': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_enabledomevarkids': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_hammerlockmovetonest': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_80.SeqEvent_RemoteEvent_1',
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            're_immediatelyopenparkdoors': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_lowerfirstbridge': [
                'Easter_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_lowersparkyselevator': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_movehammerlocktogate': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            're_movewheel': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_openparkdoors': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_raisefirstbridge': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_800.SeqEvent_RemoteEvent_4',
                'Easter_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_raisesparkyselevator': [
                'Easter_Mission_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_readyvarkhoundexplode': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            're_skipmovewheel': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_skipturnonpumps': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_skipturnonwheel': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            're_spawnfriendlybloodhound1': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            're_spawnfriendlyvarkid2': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            're_suckhammerlock': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_90.SeqEvent_RemoteEvent_8',
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_testvarkidexittunnels': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            're_testvarkidvent': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            're_testwheel': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_turnoffbeachpiratespawners': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_turnonelevators1': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
            ],
            're_turnonelevators2': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_48',
            ],
            're_turnonpumps': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_turnonstationmachines': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            're_turnonwheel': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_varkhoundtracking1': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            're_varkhoundtracking2': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            're_varkidmovetonextisland': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_killpiratesfailsafe': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_opentunneldoor': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_setfindeggbool': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_skipshipssailingin': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_skipwaterwheel': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_spawnfriendlybloodhound': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            're_startpirateship': [
                'Easter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_startstationwheel': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            're_stopperching': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_testvarkidfly': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            're_yoyo': [
                'Easter_Mission_2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'testearlspeaker': [
                'Easter_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_1060.SeqEvent_RemoteEvent_1',
            ],
            'testgate': [
                'Easter_Mission_1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
        },
        'orchid_refinery_p': {
            'raid1_activated': [
                'Orchid_Refinery_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'raid1_checklockout': [
                'Orchid_Refinery_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'raid1_missioncomplete': [
                'Orchid_Refinery_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'reapercheck': [
                'Orchid_Refinery_Raid.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'start raid music': [
                'Orchid_Refinery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'stop raid music': [
                'Orchid_Refinery_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'debugherle': [
                'Orchid_Refinery_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
        },
        'pandorapark_p': {
            'are_bearcrane': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'are_teddybearclaw_body': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Bear.SeqEvent_RemoteEvent_1',
            ],
            'are_teddybearclaw_head': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Bear.SeqEvent_RemoteEvent_0',
            ],
            'ambushcomplete': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_7',
            ],
            'bw_cleanupadds': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            'bw_secondwind': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'bw_spawnsignal': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'bloodwingdiesdebug': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_5',
            ],
            'bloodwingreset': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'bloodwingspawned': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_12',
            ],
            'bloodwingspawnedmissionactive': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'bloodwingspawnedtitlecard': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'doctorsorders_opensafe': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DoctorsOrders.Safe.SeqEvent_RemoteEvent_1',
            ],
            'doctorsorders_openstalkercage': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DoctorsOrders.StalkerCage.SeqEvent_RemoteEvent_0',
            ],
            'ep10_bwarenaelevatordisabled': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'ep10_bwarenaelevatordisabledglowing': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'ep10_bloodwinggototranqposition': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_0',
            ],
            'freewilly_freeskag': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_0',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_0',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_5',
            ],
            'freewilly_freestalker': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Stalker.SeqEvent_RemoteEvent_13',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Stalker.SeqEvent_RemoteEvent_11',
            ],
            'freewilly_freethresher': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Thresher.SeqEvent_RemoteEvent_4',
            ],
            'freewilly_guardlightswave1': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Stalker.SeqEvent_RemoteEvent_5',
            ],
            'freewilly_guardlightswave2': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Stalker.SeqEvent_RemoteEvent_1',
            ],
            'freewilly_releaseskags': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_2',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_2',
            ],
            'freewilly_sendskagsaway': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_4',
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_7',
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_9',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_4',
            ],
            'freewilly_spawnstalkerguards': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Stalker.SeqEvent_RemoteEvent_2',
            ],
            'freewilly_stalkerfightdone': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Stalker.SeqEvent_RemoteEvent_6',
            ],
            'freewilly_turnonskag1': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_1',
            ],
            'freewilly_turnonskag2': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_8',
            ],
            'freewilly_turnonskag3': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_3',
            ],
            'freewilly_turnonskagfight': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_10',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Skag.SeqEvent_RemoteEvent_6',
            ],
            'freewilly_turnonthresherfight': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Thresher.SeqEvent_RemoteEvent_3',
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Thresher.SeqEvent_RemoteEvent_4',
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Thresher.SeqEvent_RemoteEvent_1',
            ],
            'freewilly_turnonthresherguards': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Thresher.SeqEvent_RemoteEvent_2',
            ],
            'nukecheck': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            'openbloodwingcell': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_2',
            ],
            're_bloodwingcrashes': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_bloodwingmusicoff': [
                'PandoraPark_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_bloodwingmusicon': [
                'PandoraPark_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_bloodwingresetcheck': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            're_bloodwingstopresetcheck': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            're_checkwallvolume': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_checkwallvolumeelemental': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_checkwallvolumeelementalclose': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            're_checkwallvolume_dialogue': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_divebomboverride': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
            ],
            're_firegroundpound': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_gohover': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_gotonexttransition': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            're_leftdoor': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_moveout': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_moveout100': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            're_moveoutland': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            're_rightdoor': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_spawnsignal': [
                'PandoraPark_Bloodwing.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_startambush': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_5',
            ],
            'rm_releasethehounds': [
                'PandoraPark_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'readytosnipeaftermeet': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_4',
            ],
            'spawn_freewillythresher': [
                'PandoraPark_Combat.TheWorld:PersistentLevel.Main_Sequence.FreeWilly.Thresher.SeqEvent_RemoteEvent_0',
            ],
            'teleportecho': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.DoctorsOrders.LootBoxes.SeqEvent_RemoteEvent_1',
            ],
            'toggletriggeratmovepoint': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_6',
            ],
            'turnoffallplayersmessage': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_1',
            ],
            'debugbloodwing': [
                'PandoraPark_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Episode10.SeqEvent_RemoteEvent_3',
            ],
        },
        'glacial_p': {
            'activate_elevator_audio': [
                'Glacial_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'ep2_pushmission': [
                'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'ep2_rundig': [
                'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'picknewskit': [
                'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SignScripting.SeqEvent_RemoteEvent_1',
            ],
            're_playkdtitlecard': [
                'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'resetsign': [
                'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SignScripting.SeqEvent_RemoteEvent_0',
            ],
            'stop_snow_gust_audio': [
                'Glacial_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'unpausematinee': [
                'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'debugknuckledragger1': [
                'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'debugknuckledragger2': [
                'Glacial_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
        },
        'dungeonraid_p': {
            're_bossreset': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_bridge_complete': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_bridge_extend': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_bridge_retract': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_chestcleanup': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_chestunlock': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            're_disable_bossreset': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_fire_concentric': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_fire_cycle': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            're_fire_doublecycle': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_fire_everything': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_fire_lefttoright': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_fire_random': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_fire_righttoleft': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_fire_stopall': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_killbasilisks': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_lockdown': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_lockdownover': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_lootspew': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_mimicspawnedfromchest': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_raidpit_quickoff': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_resetglow': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            're_spawnraidbeast': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_statesaver_door_closed': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_statesaver_door_closing': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_statesaver_door_open': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_statesaver_door_opening': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_storebasiliskrefs': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            're_summonraidbeast': [
                'DungeonRaid_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_torguedialog_04': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            're_torguedialog_05': [
                'DungeonRaid_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
        },
        'orchid_saltflats_p': {
            'hovercraftspawned': [
                'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.CombatLevelChallenges.SeqEvent_RemoteEvent_0',
            ],
            'lighthousebeam_enabled': [
                'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'orchid_endgame_missionstart': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Lighthouse_Active.SeqEvent_RemoteEvent_0',
            ],
            'orchid_m4_kickoff': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'orchid_m4_turnin': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'orchid_m5_boxpickedup': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'orchid_m5_kickoff': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            'orchid_m7_turnin': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'orchid_m8_compassassembled': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'orchid_m8_compasspiecetaken': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'orchid_m8_compasstaken': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'orchid_m8_givecompasspiece': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'orchid_m8_givecompasspieceidle': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'orchid_sm_scurvydogs_activatefruittrees': [
                'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'orchid_sm_scurvydogs_disablefruittrees': [
                'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'orchid_sm_smellsvictory_killshivspike': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'race_beacon_1_active': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'race_beacon_1_reached': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'race_beacon_2_active': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'race_beacon_2_reached': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'race_beacon_3_active': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            'race_beacon_3_reached': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            'race_beacon_4_active': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            'race_beacon_4_reached': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
            ],
            'race_beacon_5_active': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_44',
            ],
            'race_beacon_5_reached': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_45',
            ],
            'race_finalbeacon_active': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
            ],
            'race_finalbeacon_reached': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_47',
            ],
            'race_startbeacon_active': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_48',
            ],
            'race_startbeacon_reached': [
                'Orchid_SaltFlats_Race.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            'randomhovercraftactive': [
                'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'refinerylift01_enable': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'refinerylift01_floor1': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'refinerylift01_floor2': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'refinerylift01_switch_used': [
                'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'refinerylift02_enable': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'refinerylift02_floor1': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'refinerylift02_floor2': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'refinerylift_glow_disable': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'refinerylift_glow_enable': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'sunrise_end': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'sunrise_start': [
                'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'sunset_end': [
                'Orchid_SaltFlats_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'testkill': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Lighthouse_Active.SeqEvent_RemoteEvent_2',
            ],
            'turn_off_music': [
                'Orchid_SaltFlats_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'wurmbellyexitactive': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'debugleviathan': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Lighthouse_Active.SeqEvent_RemoteEvent_1',
            ],
            'debugscarlet': [
                'Orchid_SaltFlats_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PirateQueen_Intro.SeqEvent_RemoteEvent_0',
            ],
        },
    },
    'TPS': {
        'moonslaughter_p': {
            'closearenadorrs': [
                'MoonSlaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'lowerelevator': [
                'MoonSlaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'openarenadoors': [
                'MoonSlaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'roundfinish': [
                'MoonSlaughter_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'roundstart': [
                'MoonSlaughter_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
        },
        'ma_leftcluster_p': {
            'activatenexuswaypoint': [
                'Ma_LeftCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'activate_download': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'allclear': [
                'Ma_LeftCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_4',
            ],
            'badmemorydestroyed': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MissionFlowEvents.SeqEvent_RemoteEvent_0',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MissionFlowEvents.SeqEvent_RemoteEvent_2',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MissionFlowEvents.SeqEvent_RemoteEvent_3',
            ],
            'blowbubbles': [
                'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'bridgeconstructionstart': [
                'Ma_LeftCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'cookieattacked': [
                'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'copydigger': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MissionFlowEvents.SeqEvent_RemoteEvent_12',
            ],
            'destroytassiter': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'diggermoved': [
                'Ma_LeftCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_1',
            ],
            'diggerstarted': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MissionFlowEvents.SeqEvent_RemoteEvent_1',
            ],
            'disableminebugs': [
                'Ma_LeftCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'downloadhsource': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'hsourcealarm': [
                'Ma_LeftCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'hsourcedownload': [
                'Ma_LeftCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'holo_zed1': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'leftcluster_turnononewayswitch': [
                'Ma_LeftCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'lilith_appear': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            'lilith_appear_vo_end': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'lilith_badsector1': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            'lilith_badsector2': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'lilith_badsector3': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'lilith_vo_piece3': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_26',
            ],
            'locatebridgepiece1': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MissionFlowEvents.SeqEvent_RemoteEvent_4',
            ],
            'memoryconsoleuse1': [
                'Ma_LeftCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'memoryconsoleuse2': [
                'Ma_LeftCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'memoryconsoleuse3': [
                'Ma_LeftCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'memoryconsoleused': [
                'Ma_LeftCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'pastedigger': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_7',
            ],
            'shameattacked': [
                'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'tp_tannisneardigger': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'talkedtoshame': [
                'Ma_LeftCluster_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'tannis_appear': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'tassiterfuse': [
                'Ma_LeftCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'tassiteroff': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_2',
            ],
            'tassiter_dead': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'vo_badsectorintro': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_13',
            ],
            'vo_bridgereconstructing': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_5',
            ],
            'vo_bridgerecovered': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_14',
            ],
            'vo_consolerdy': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            'vo_consoleuse1': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_0',
            ],
            'vo_consoleuse2': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_8',
            ],
            'vo_deadbattery': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_18',
            ],
            'vo_entermemory': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_6',
            ],
            'vo_forbridge1done': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MissionFlowEvents.SeqEvent_RemoteEvent_8',
            ],
            'vo_freepiece1': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_12',
            ],
            'vo_getpiece1': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_22',
            ],
            'vo_hsourceintro': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_17',
            ],
            'vo_lilithjump': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_21',
            ],
            'vo_memorymadness': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_16',
            ],
            'vo_pathunblock': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_11',
            ],
            'vo_piece1taken': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_15',
            ],
            'vo_piecescollected': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_23',
            ],
            'vo_quarantine': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_19',
            ],
            'vo_tassiterannounce': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_10',
            ],
            'vo_vaultintro': [
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_9',
            ],
            'zedtocave': [
                'Ma_LeftCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Ma_LeftCluster_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_Dialog.SeqEvent_RemoteEvent_3',
            ],
        },
        'ma_rightcluster_p': {
            '200_corruptdata_bannerdestroyed': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'arenacollapseevent': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'arenadestruction_2ndexplosion': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'arenadestruction_firstexplosion': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'arenaposterremoved': [
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'churchfiresfx1': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'churchfiresfx2': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'churchfiresfx3': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'churchfiresfx4': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'churchfire_vo': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_45',
            ],
            'codewormswallowskey_ended': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'codewormunborrow': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'crowdcheerwallstart': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'dannydialoguestarted': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'debugtimeofdayreset': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            'denialsubroutine25percenthp': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'denialsubroutine50percenthp': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'denialsubroutine75percenthp': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'donkvsclaptrap': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            'donkvsclaptrap_ended': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_30',
            ],
            'entranceposter1_removed': [
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'entranceposter2_removed': [
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'happymusic_off': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'happymusic_on': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'hide_corruptionlevel': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'initiated_teleportfrom_denialsubroutine': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'initiated_teleportto_denialsubroutine': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'karimadialoguecompleted': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_3',
            ],
            'memoryconsoleactivatedsuccess': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'memorystatushpplus5': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'nearbotpit': [
                'Ma_RightCluster_SideMission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'nukeexplosion': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'picklegunchestopened': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'placardciv1_restored': [
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'placardciv2_restored': [
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'reboot': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'reboot0_civ_events': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_0',
            ],
            'reboot1_civ_events': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_17',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_19',
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'reboot1_completed': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'reboot2_civ_events': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_1',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_15',
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'reboot2_completed': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'reboot3_civ_events': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_16',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_18',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_2',
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Ma_RightCluster_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'reboot3_completed': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            'rebootcompleted': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'removecivwithplacard': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_28',
            ],
            'removereboot0onlycivs': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.Civilians_States.SeqEvent_RemoteEvent_27',
            ],
            'rescueddamsel': [
                'Ma_RightCluster_SideMission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'sadmusic_on': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'teleportout': [
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
                'Ma_RightCluster_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'totallydoomedintro': [
                'Ma_RightCluster_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
        },
        'spaceport_p': {
            'aidef_handsomejack_jackfinishedfasttravel': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'ambientaireachedgoal': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'audio_elecfence_off': [
                'Spaceport_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'audio_holo_off': [
                'Spaceport_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'audio_holo_on': [
                'Spaceport_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'bartrapambientpathing': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'bartrapspawned': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_47',
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_48',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_49',
            ],
            'blockedelevatorvo': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'challengefinetaken': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'challenge_trashburnt': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'chp03_playerscreamcomplete': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'chp7_givefasttraveltohelios': [
                'Spaceport_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'closedeconentrancedoor': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_69',
            ],
            'closedeconexitdoor': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            'closeforcefieldsidedoor': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_74',
            ],
            'closeliftlowerdoor': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'closeliftupperdoor': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'closeninadecondoor': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_54',
            ],
            'closesecretentrance': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'customsclaptrapspawned': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_45',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_47',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_56',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_63',
            ],
            'customstrapidle': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'deployelevatorturrets': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_72',
            ],
            'destroymoxxi': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'dialog_jackturninlinecomplete': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'disabledefaultelevatorscripting': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'disableforcefield': [
                'Spaceport_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'disablemerriflift': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'disablepasquiggles': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'dish1play': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            'dish1state0': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'dish2play': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
            ],
            'dish2state0': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            'dish2state1': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            'dish3play': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'dish3state0': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
            ],
            'dish3state1': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            'enabledefaultelevatorscripting': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'enableforcefield': [
                'Spaceport_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'enablemerrifelevatorswitch': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'enablemerriflift': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'enablepasquiggles': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'finishednurseninatitlecard': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_53',
            ],
            'firestationbeam': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'force_music_quiet': [
                'Spaceport_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'grinderclosing': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'grinderopening': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'grindertrayopening': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'jackbarscenesetup': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'lil_stopidle': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'lilithdance': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'lilithstopdance': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_75',
            ],
            'lockdown': [
                'Spaceport_Town.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'lockskybridgelobbydoor': [
                'Spaceport_Town.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'logwoodused': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.RoughLove.SeqEvent_RemoteEvent_5',
            ],
            'm3takendamagefrommelee': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_89',
            ],
            'm_chp03_barcontinuevh1vo': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'm_chp03_blackmarketclosed': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_44',
            ],
            'm_chp03_claptrapgivingticket': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_65',
            ],
            'm_chp03_closeofficedoor': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'm_chp03_crazyearlvoplay': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_64',
            ],
            'm_chp03_disableelevator': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'm_chp03_electricfenceshutdown': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
            ],
            'm_chp03_enablefenceswitch': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_52',
            ],
            'm_chp03_firstm3vo': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'm_chp03_followmoxxi': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'm_chp03_hitm3': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_50',
            ],
            'm_chp03_liftused': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'm_chp03_lilithtalkedto': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'm_chp03_movelilithtobar': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'm_chp03_movemoxxitobackroom': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            'm_chp03_moverolandtobar': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'm_chp03_moxxisecretdoorstartopen': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_88',
            ],
            'm_chp03_moxxitalkedto': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'm_chp03_moxxititlecardcomplete': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'm_chp03_moxxititlecardstart': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'm_chp03_objset03_followclaptrap': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'm_chp03_openofficedoor': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'm_chp03_orbatronobjactivated': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'm_chp03_orbatrontakenanimcomplete': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'm_chp03_placeturretpart': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_55',
            ],
            'm_chp03_powerswitchused': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_59',
            ],
            'm_chp03_reverseelevator': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'm_chp03_rolandtalkedto': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'm_chp03_stompm3': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_48',
            ],
            'm_chp03_transmitterbought': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_57',
            ],
            'm_chp04_findclapjackspawned': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'm_chp04_jackandclapofflift': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'm_chp04_liftused': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'm_chp04_spawnjack': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'm_chp3_m3hit1stm3vocomplete': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_60',
            ],
            'm_chp4_customtrapsinterupted': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'm_chp4_interuptcomplete': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'm_chp4_leveltansopen': [
                'Spaceport_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'movemoxxitobackroom': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_83',
            ],
            'moxxislotmachineused': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'moxxispawned': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_51',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_58',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_61',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_62',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_76',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_78',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_79',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_80',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_90',
            ],
            'moxxi_stoparmsidle': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'opendeconentrancedoor': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_68',
            ],
            'opendeconexitdoor': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            'openforcefieldsidedoor': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_87',
            ],
            'openliftlowerdoor': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'openliftupperdoor': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'openninadecondoor': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'openninamaindoor': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'opensecretentrance': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'playm3helpvo': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'playm3helpvocomplete': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_66',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_71',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_73',
            ],
            'playnishastart': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.NishaECHOs.SeqEvent_RemoteEvent_1',
            ],
            'playnurseninatitlecard': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'playermoved': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_67',
            ],
            'release_music_volume': [
                'Spaceport_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'roland_stopidle': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'rotatedish': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'setdeconentrancedoorclosed': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_70',
            ],
            'setdeconexitdoorclosed': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'setelevatortotop': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'setforcefieldsidedoorclosed': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_81',
            ],
            'setninadecondoorclosed': [
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'slotmachinebuttonused': [
                'Spaceport_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_77',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_77',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_82',
            ],
            'spawndefaultai': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'spawnmoxxibar': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'spawnmoxxiworkshop': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_84',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_85',
            ],
            'startmoxxibarsceneidle': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'stationbeamfired': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'stoprolandcrossarm': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'swapbarbot': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'swapmerrifstatue': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WipingSlate.SeqEvent_RemoteEvent_2',
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WipingSlate.SeqEvent_RemoteEvent_3',
            ],
            'teleportmainsaway': [
                'Spaceport_Town.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'teleportmainsback': [
                'Spaceport_Town.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'toarms_opencurtains': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.ToArms.SeqEvent_RemoteEvent_0',
            ],
            'turnmerrifhologramoff': [
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'turnonmoxxispark': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_86',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_86',
            ],
            'turnoffmoxxispark': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Spaceport_M_Chp3.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'turnonbarperches': [
                'Spaceport_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'Spaceport_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'unlockskybridgelobbydoor': [
                'Spaceport_Town.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'wipingslate_giveechodj': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WipingSlate.SeqEvent_RemoteEvent_1',
            ],
            'wipingslate_jackendline': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WipingSlate.SeqEvent_RemoteEvent_5',
            ],
            'wipingslate_startmusic': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WipingSlate.SeqEvent_RemoteEvent_0',
            ],
            'wipingslate_stopmusic': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.WipingSlate.SeqEvent_RemoteEvent_4',
            ],
            'zapped3_claptrapdies': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.Zapped.SeqEvent_RemoteEvent_0',
            ],
            'playnishaechocomplete': [
                'Spaceport_SideMissions.TheWorld:PersistentLevel.Main_Sequence.NishaECHOs.SeqEvent_RemoteEvent_0',
            ],
        },
        'ma_subboss_p': {
            'audiodrilldown': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'beamstart': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'bossmusicstart': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'bossmusicstop': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'checkmutatorinitialobjectives': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'closeportals': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_63',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'difficultyeasy': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            'difficultyhard': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            'difficultytut0': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'disablegc': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
            ],
            'disablemutatoractivator': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'disablemutatormachines': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            'drillstart': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'enablegc': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            'enablemutatoractivator': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'enablemutatormachines': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'enablemutatormachinesconditional': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'enablevacuum': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'failmutatormission': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_63',
            ],
            'gametut0': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'gametut1': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'gametut2': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'gametut3': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'gametut4': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'gametut5': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'gametut6': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'gametut7': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'gametut8': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            'gametut9': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'godrill': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Ma_SubBoss_Drill.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'hsourceoff': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'incrementkillstreak': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_53',
            ],
            'levelloadpostdrill': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'levelloadpredrill': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'machinecancel': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
            ],
            'machinechangemode': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_44',
            ],
            'machinecommit': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
            ],
            'machinedecreasedifficulty': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_45',
            ],
            'machineincreasedifficulty': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_49',
            ],
            'modtut0': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'modtut1': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'modtut2': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'modtut3': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'modtut4': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'modtut5': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'modtut6': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_57',
            ],
            'modtut7': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'modtut8': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'modtut9': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'mutatoraudio': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'opendeck13transition': [
                'Ma_SubBoss_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'openportal1': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'openportal2': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'openportal3': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'openportal4': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'openportal5': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'openportal6': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'openportals': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_8',
            ],
            'open_fakeexit': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'pickwave': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_0',
            ],
            'questturnin': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_50',
            ],
            're_took_hsource': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter_05.SeqEvent_RemoteEvent_0',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter_05.SeqEvent_RemoteEvent_1',
            ],
            'resetportals': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'roundfinish': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_20',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_5',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_7',
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'slaughtercrithit': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_56',
            ],
            'slaughtercritkill': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_55',
            ],
            'slaughterend1stwave': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_61',
            ],
            'slaughterend2ndwave': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_54',
            ],
            'slaughterend3rdwave': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_52',
            ],
            'slaughterkill': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_51',
            ],
            'slaughterkillstreak': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_47',
            ],
            'slaughterlootchest': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_48',
            ],
            'slaughterplcrit': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'slaughterpldies': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            'slaughterpldown': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'slaughterstart1stwave': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            'slaughterstart2ndwave': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            'slaughterstart3rdwave': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'startmutator': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_21',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_4',
            ],
            'startwave1': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_18',
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_60',
            ],
            'startwave2': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_19',
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_59',
            ],
            'startwave3': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_17',
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'start_bugs_wave1': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_F_Bugs.SeqEvent_RemoteEvent_3',
            ],
            'start_bugs_wave2': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_F_Bugs.SeqEvent_RemoteEvent_4',
            ],
            'start_bugs_wave3': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_F_Bugs.SeqEvent_RemoteEvent_0',
            ],
            'start_dawgs_wave1': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_C_Dawgs.SeqEvent_RemoteEvent_3',
            ],
            'start_dawgs_wave2': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_C_Dawgs.SeqEvent_RemoteEvent_4',
            ],
            'start_dawgs_wave3': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_C_Dawgs.SeqEvent_RemoteEvent_0',
            ],
            'start_fragmented_wave1': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_A_Fragmented.SeqEvent_RemoteEvent_3',
            ],
            'start_fragmented_wave2': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_A_Fragmented.SeqEvent_RemoteEvent_4',
            ],
            'start_fragmented_wave3': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_A_Fragmented.SeqEvent_RemoteEvent_0',
            ],
            'start_glitches_wave1': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_E_Glitches.SeqEvent_RemoteEvent_3',
            ],
            'start_glitches_wave2': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_E_Glitches.SeqEvent_RemoteEvent_4',
            ],
            'start_glitches_wave3': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_E_Glitches.SeqEvent_RemoteEvent_0',
            ],
            'start_insec_wave1': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_B_Insec.SeqEvent_RemoteEvent_3',
            ],
            'start_insec_wave2': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_B_Insec.SeqEvent_RemoteEvent_4',
            ],
            'start_insec_wave3': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_B_Insec.SeqEvent_RemoteEvent_0',
            ],
            'start_viruses_wave1': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_D_Viruses.SeqEvent_RemoteEvent_3',
            ],
            'start_viruses_wave2': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_D_Viruses.SeqEvent_RemoteEvent_4',
            ],
            'start_viruses_wave3': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.Waves_D_Viruses.SeqEvent_RemoteEvent_0',
            ],
            'steam': [
                'Ma_SubBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'turnjumppadoff': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter_05.SeqEvent_RemoteEvent_6',
            ],
            'turnjumppadon': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter_05.SeqEvent_RemoteEvent_3',
            ],
            'unhidewalls': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'unlockchests': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_58',
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'wavecomplete': [
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_1',
                'Ma_SubBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Mutator_Slaughter.SeqEvent_RemoteEvent_2',
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'drilldown': [
                'Ma_SubBoss_Drill.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'killaion': [
                'Ma_SubBoss_Mutator.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_62',
            ],
        },
        'comfacility_p': {
            'anotherpickleenablewaves': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'anotherpicklewave1dead': [
                'ComFacility_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'backup_spawngatebandits': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_10',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_2',
            ],
            'bellykilledlast': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_12',
            ],
            'closeentrancegate': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_16',
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'controlroomdoordisable': [
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Dynamic.SeqEvent_RemoteEvent_0',
            ],
            'controlroomdoorenable': [
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Dynamic.SeqEvent_RemoteEvent_6',
            ],
            'courtyardgateopened': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'dropbagstick': [
                'ComFacility_SideMissions.TheWorld:PersistentLevel.Main_Sequence.EmptyBillabong.SeqEvent_RemoteEvent_2',
            ],
            'entryfight_spawnpsychogarage': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_26',
            ],
            'entryfight_startcombat': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_17',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_18',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_19',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_20',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_25',
            ],
            'firestationbeam': [
                'ComFacility_Sky.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'hidehologramglow': [
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'initialcombatresolved': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_0',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_0',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_5',
            ],
            'm_chp04_closemidgetdoor': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_10',
            ],
            'm_chp04_consolehacked': [
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'm_chp04_destroyturrets': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_9',
            ],
            'm_chp04_enteredcourtyardlines': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_19',
            ],
            'm_chp04_enteredcourtyardlinescomplete': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'm_chp04_fullyopenmidgetdoor': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_11',
            ],
            'm_chp04_initialredbellylines': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_14',
            ],
            'm_chp04_initialredbellylinescomplete': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_14',
            ],
            'm_chp04_midgetdooropen': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_UpperFloorGply.SeqEvent_RemoteEvent_12',
            ],
            'm_chp04_openmidgetdoor': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_9',
            ],
            'm_chp04_openturret': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_5',
            ],
            'm_chp04_redspawned': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'm_chp04_releasegateguards': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_15',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_21',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_3',
            ],
            'm_chp04_startturretlights': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_7',
            ],
            'm_chp04_stopturretlights': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_6',
            ],
            'm_chp04_turretdestroyedlines': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_29',
            ],
            'm_chp04_turretdestroyedlinescomplete': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_24',
            ],
            'm_chp4_bypassedgate': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_24',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_30',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_14',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_8',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_11',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_24',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_27',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_28',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_30',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_31',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_32',
            ],
            'm_chp04_bellydead': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_6',
            ],
            'm_chp04_reddead': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_8',
            ],
            'opencomsdish': [
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'opencourtyardgate': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_15',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_4',
            ],
            'opencrisisscartomoongate': [
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'openentrancegate': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_12',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_13',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_16',
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_spawnbadassspaceman': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_UpperFloorGply.SeqEvent_RemoteEvent_1',
            ],
            're_spawnjetpackfliers': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_UpperFloorGply.SeqEvent_RemoteEvent_2',
            ],
            'redkilledlast': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_10',
            ],
            'redseparationjump': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'redspawnadditionalenemies': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'relaydestroyed': [
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ActivateRelay.SeqEvent_RemoteEvent_7',
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ActivateRelay_0.SeqEvent_RemoteEvent_7',
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ActivateRelay_1.SeqEvent_RemoteEvent_7',
            ],
            'scavwalla_charge_start': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'scavwalla_charge_stop': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'scavwalla_cheer_start': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'scavwalla_cheer_stop': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'scavwalla_disappoint_start': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'scavwalla_disappoint_stop': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'scavwalla_start': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'scavwalla_stop': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'searchswagman': [
                'ComFacility_SideMissions.TheWorld:PersistentLevel.Main_Sequence.EmptyBillabong.SeqEvent_RemoteEvent_3',
            ],
            'setcourtyardgateclose': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_2',
            ],
            'setentrancegateopen': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Courtyard_Gply.SeqEvent_RemoteEvent_3',
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'showhologramglow': [
                'ComFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'sky_turnofflighting': [
                'ComFacility_Sky.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'sky_turnonlighting': [
                'ComFacility_Sky.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'spawn_scavboss': [
                'ComFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'startbabykragonmat': [
                'ComFacility_SideMissions.TheWorld:PersistentLevel.Main_Sequence.EmptyBillabong.SeqEvent_RemoteEvent_0',
            ],
            'stationbeamfired': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_11',
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_Chp4.SeqEvent_RemoteEvent_3',
            ],
            'turretcoversopen': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.ComFacility_GateGply.SeqEvent_RemoteEvent_13',
            ],
            're_spawnredbellyproxy': [
                'ComFacility_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
        },
        'ma_deck13_p': {
            'digisim_entrance_revealed': [
                'Ma_Deck13_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'digistruct_all_players': [
                'Ma_Deck13_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'hsource_locked': [
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'jack_at_console': [
                'Ma_Deck13_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'ma_ch06_re_reactivateconsole': [
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'playendslideshow': [
                'Ma_Deck13_Intro_SS.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'playendslideshow_finished': [
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'player_entered_digipad': [
                'Ma_Deck13_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'playercheck_add': [
                'Ma_Deck13_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'playercheck_remove': [
                'Ma_Deck13_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_closingcredits': [
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'reveal_digisim_entrance': [
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'reveal_password_path': [
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'showextrascreens': [
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'showhsource': [
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'slideshowcomplete': [
                'MA_DECK13_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Ma_Deck13_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'started_digisim_loader': [
                'MA_DECK13_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'turn_on_leveltransition': [
                'Ma_Deck13_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
        },
        'ma_finalboss_p': {
            'activate_levelexit': [
                'Ma_FinalBoss_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'eos_40percenthealth': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'eos_75percenthealth': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'eos_dying': [
                'Ma_FinalBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Platform_Panic.SeqEvent_RemoteEvent_1',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Platform_Panic.SeqEvent_RemoteEvent_4',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Platform_Panic.SeqEvent_RemoteEvent_5',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.Platform_Panic.SeqEvent_RemoteEvent_6',
            ],
            'eos_holotauntcomplete': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'eos_homingorbreached': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'eos_iwanttomoonshot': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'eos_iwanttoresumepatrolling': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'eos_reset': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'eos_spawned': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            'eos_startingrecharge': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            'eos_tauntfinished': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'eclipse_spawned': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            'finalboss_turnononewayswitch': [
                'Ma_FinalBoss_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'forcecombatmusic': [
                'Ma_FinalBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'hide_throneroom_level': [
                'Ma_FinalBoss_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'jack_arrived': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'pick_new_taunt': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_throne_titlecard': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_throne_titlecard_finished': [
                'Ma_FinalBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'taunttimercomplete': [
                'Ma_FinalBoss_Game.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
        },
        'innercore_p': {
            'activateophas': [
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'activateplantenemygrp001': [
                'InnerCore_p.TheWorld:PersistentLevel.Main_Sequence.Combat.SeqEvent_RemoteEvent_0',
                'InnerCore_p.TheWorld:PersistentLevel.Main_Sequence.Combat.SeqEvent_RemoteEvent_1',
            ],
            'audio_start_ring_audio': [
                'InnerCore_geo_02.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'boss_fight_music_off': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'boss_fight_music_on': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'deactivateophas': [
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'entereleseervo': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'jacksmalltalk02': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'killophasuperior': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'InnerCore_OPHATitleCard.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'lilithfollow': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'movetobadass': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'movetoheavy': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'movetosuperior': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'ophasdied': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'plotdialog01': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'plotdialog02': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'plotdialog03': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'plotdialog04': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'plotdialog05': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_closecrystalcrack': [
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_closingcredits': [
                'Vault_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_closingcreditsreturn': [
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_deactivatemoonstonealtars': [
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_disableboss1cover': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_disablebossammo': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_disablebossspawnvolumetesting': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_disablefacebossbar': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_disablefloorislava': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_disableinnercoreenemies': [
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_disableminiondenreset': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_enableboss1cover': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            're_enablebossammo': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_enablefloorislava': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_enableminiondenreset': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_enablevaultexit': [
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_fbcbigdead': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            're_finalbossdeathmission': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            're_finalbossdeathrunnable': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            're_finalbosstitlecardreturnmission': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            're_finalbosstitlecardreturnrunnable': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            're_initfinalbossmission': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            're_initfinalbossrunnable': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            're_initraidbossmission': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            're_initraidbossrunnable': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            're_israidmissionpaymoonstones': [
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_opencrystalcrack': [
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_opencrystalcrackraid': [
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_raidbossdeathmission': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            're_raidbossdeathrunnable': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
            ],
            're_raidbosslavafloorquickie': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_raidbosslavafloorquickielonger': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            're_raidbosslavafloorquickielongest': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            're_raidbosstitlecardreturnmission': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
            ],
            're_raidbosstitlecardreturnrunnable': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_44',
            ],
            're_setcurrentfacebossbar': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_testisraidmissionorrunnable': [
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_unhidevaultarch': [
                'Vault_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            're_vaultbossstageonetitlecard': [
                'Vault_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_vaultbossstageonetitlecard_return': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'smallbossteleportlocation': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'spawnsmallbossadds': [
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Vault_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'stairs': [
                'InnerCore_p.TheWorld:PersistentLevel.Main_Sequence.MissionProgression.SeqEvent_RemoteEvent_0',
            ],
            'sterwinforeverkickoff': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'stirwindialog01': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'stirwindialogbad2': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'InnerCore_OPHATitleCard.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'stirwindialograndom': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'titlecard': [
                'InnerCore_OPHATitleCard.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'turnonbadassopha': [
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'turnonheavyopha': [
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'turnonregopha': [
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'turnonsupeopha': [
                'InnerCore_OPHATitleCard.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'yougofirst': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'cplbest00': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'InnerCore_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'cplbest01': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'InnerCore_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'InnerCore_combat00.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'cplbest02': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'InnerCore_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'cplbest03': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'InnerCore_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'cplbest04': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'InnerCore_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'cplbest05': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
                'InnerCore_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'disablecylindercollision': [
                'InnerCore_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'hitstirwinaudio': [
                'InnerCore_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
        },
        'laserboss_p': {
            'boss_fight_music_off': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'boss_fight_music_on': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'eyecycleanims': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'eyeopened': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Meet_Jack.SeqEvent_RemoteEvent_0',
            ],
            'eyeballreactions': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_2',
            ],
            'floor_slag_flow_tube_1': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'floor_slag_flow_tube_2': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'floor_slag_flow_tube_3': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'floor_slag_flow_tube_4': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'hose_distress_start': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'hose_distress_stop': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            'hose_distress_uber_start': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            'hose_distress_uber_stop': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'hose_happy_start': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'hose_happy_stop': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'hose_idle_start': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'hose_idle_stop': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'hose_opening_start': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'hose_opening_stop': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'hose_sleep_start': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'hose_sleep_stop': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_afterfire_curiousvox': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            're_allcolzmechminionsdead': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_colzdeath': [
                'LaserBoss_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_colzdeath_return': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_colzmech_fakedeath': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_colztitlecardmech': [
                'LaserBoss_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_colztitlecardmech_return': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_colztitlecardzealot': [
                'LaserBoss_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_colztitlecardzealot_return': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_debugeye': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_debugeyeanims': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_destroycolzmechminions': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_destroycolzminions': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_disableelectrohallway': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_3',
            ],
            're_disableminiondenreset': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_disableregeratingbossammo': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            're_enableelectrohallway': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_2',
            ],
            're_enablelaserfireloop': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_8',
            ],
            're_enableminiondenreset': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_enableregeratingbossammo': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_jackopenselevatordoor': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Doors_And_Elevators.SeqEvent_RemoteEvent_0',
            ],
            're_nicetomeetyou': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_pause_injections': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            're_playercrossedelectrohallway': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.ElectroHallway.SeqEvent_RemoteEvent_0',
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.ElectroHallway.SeqEvent_RemoteEvent_1',
            ],
            're_resume_injections': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            're_scriptedfirelaser': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_9',
            ],
            're_scriptedlaser_electro': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            're_scriptedlaser_electro_stop': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_48',
            ],
            're_setcurrentplatefull': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_setcurrentplatepartial': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_slag_inject': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_stoplaserfireloop': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_5',
            ],
            're_testforallcolzmechminionsdead': [
                'LaserBoss_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_addwaypoint': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_8',
            ],
            're_dialog_enableechoproxy1': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.CoreIntro.SeqEvent_RemoteEvent_1',
            ],
            're_dialog_enableechoproxy2': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.CoreIntro.SeqEvent_RemoteEvent_0',
            ],
            're_dialog_moxxieareyousure': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_4',
            ],
            're_eyeballdonebeinghappy': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Meet_Jack.SeqEvent_RemoteEvent_9',
            ],
            're_eyeballdonefiring': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Meet_Jack.SeqEvent_RemoteEvent_8',
            ],
            're_eyeballshutdown': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_16',
            ],
            're_firingwhileopen': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_7',
            ],
            're_hurtaudio_1': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            're_hurtaudio_2': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            're_hurtaudio_3': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            're_injection1started': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_9',
            ],
            're_injection2started': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_13',
            ],
            're_injection3started': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_14',
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_15',
            ],
            're_jackspawned': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_laserfiringrumble': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_11',
            ],
            're_removewaypoint': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_0',
            ],
            're_rotring_laserfiring': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_1',
            ],
            're_rotring_laserstartfiring': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            're_rotring_laserstopfiring': [
                'LaserBoss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_47',
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_0',
            ],
            're_startblackholeeffects': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_5',
            ],
            're_startshutdowninstructiondialog': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_1',
            ],
            're_stopblackholeeffects': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_3',
            ],
            're_upsetrumble_lv1_start': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_6',
            ],
            're_upsetrumble_lv1_stop': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_13',
            ],
            're_upsetrumble_lv2_start': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_12',
            ],
            're_upsetrumble_lv2_stop': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.Laser_And_Rumble.SeqEvent_RemoteEvent_10',
            ],
            're_eye_rumblefx1': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_12',
            ],
            're_eye_rumblefx2': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_10',
            ],
            're_flowfx1': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_11',
            ],
            're_flowfx2': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_7',
            ],
            're_flowfx3': [
                'LaserBoss_Mission.TheWorld:PersistentLevel.Main_Sequence.EyeShutdownPrep.SeqEvent_RemoteEvent_6',
            ],
        },
        'moonshotintro_p': {
            'audio_sparkaudio': [
                'MoonShotIntro_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'backuptimerflameknucklefight': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'backuptimerflameknucklefight_abort': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'beckon': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'beckon_done': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'beginexplosions': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Explosions.SeqEvent_RemoteEvent_6',
            ],
            'ch1b_renamedriders': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'ch1_jack_downstate': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'ch1_jack_playerrevived': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'flameknuckle_stage2': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'followclaptrap': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'jetpacksdead': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            're_activatetopmoonshotressurectstation': [
                'MoonShotIntro_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_colzguardiantitle_finished': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Explosions.SeqEvent_RemoteEvent_5',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.OneOffs.SeqEvent_RemoteEvent_5',
            ],
            're_colzguardiantitle_start': [
                'MoonShotIntro_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Explosions.SeqEvent_RemoteEvent_1',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.OneOffs.SeqEvent_RemoteEvent_1',
            ],
            're_commandroom_sendanothercrate': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.OneOffs.SeqEvent_RemoteEvent_7',
            ],
            're_dahlbeganshooting': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_doneexplainingmoonshot': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_elevator_fixed': [
                'MoonShotIntro_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_flameknuckletitle_finished': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Explosions.SeqEvent_RemoteEvent_4',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.OneOffs.SeqEvent_RemoteEvent_4',
            ],
            're_flameknuckletitle_start': [
                'MoonShotIntro_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Explosions.SeqEvent_RemoteEvent_0',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.OneOffs.SeqEvent_RemoteEvent_0',
            ],
            're_getintobulletthing': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_jackhasspawned': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            're_jackmoveaftertassiter': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_jacktitle_finished': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Explosions.SeqEvent_RemoteEvent_3',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.OneOffs.SeqEvent_RemoteEvent_3',
            ],
            're_jacktitle_start': [
                'MoonShotIntro_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Explosions.SeqEvent_RemoteEvent_2',
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.OneOffs.SeqEvent_RemoteEvent_2',
            ],
            're_movejackpastdoor': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_TassiterAndJack.SeqEvent_RemoteEvent_19',
            ],
            're_movetomoonshot_onload': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_readytobemoonshot': [
                'MoonShotIntro_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_securityvofinished': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.OneOffs.SeqEvent_RemoteEvent_8',
            ],
            're_securityvo_started': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.OneOffs.SeqEvent_RemoteEvent_6',
            ],
            're_startclaptrapfailsafe': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'setmusicstateambient': [
                'MoonShotIntro_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'setmusicstatecombat': [
                'MoonShotIntro_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'statesave_fleeclaptraponload': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_changejacktargetable': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_consoledestroyed': [
                'MoonShotIntro_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
        },
        'eridian_slaughter_p': {
            'allo2on': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.GravVacAndHazardControl_0.SeqEvent_RemoteEvent_2',
            ],
            'badassroundskillcheck': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'badassroundskillend': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'badassroundskillstart': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'buttons': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective3.SeqEvent_RemoteEvent_6',
            ],
            'chesttest': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective5.SeqEvent_RemoteEvent_4',
            ],
            'closeroof': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'closeroof_audio': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'destroyfelicity': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective2.SeqEvent_RemoteEvent_3',
            ],
            'fail': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective3.SeqEvent_RemoteEvent_4',
            ],
            'failed': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_22',
            ],
            'gathered': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_3',
            ],
            'givekeys': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective5.SeqEvent_RemoteEvent_3',
            ],
            'goo': [
                'Eridian_slaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.EridianSlaughterRound01.SeqEvent_RemoteEvent_0',
            ],
            'hidefelicity': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective2.SeqEvent_RemoteEvent_0',
            ],
            'jump': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective1.SeqEvent_RemoteEvent_1',
            ],
            'm1_loop1': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Mission1.SeqEvent_RemoteEvent_4',
            ],
            'm2_loop1': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Mission2.SeqEvent_RemoteEvent_3',
            ],
            'm3_loop1': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Mission3.SeqEvent_RemoteEvent_4',
            ],
            'm4_loop1': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Mission4.SeqEvent_RemoteEvent_4',
            ],
            'm5_loop1': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Mission5.SeqEvent_RemoteEvent_3',
            ],
            'mba_loop1': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.MissionBadass.SeqEvent_RemoteEvent_3',
            ],
            'openroof': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'openroof_audio': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'optionalobj_turnofflaserarea': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'physon': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective5.SeqEvent_RemoteEvent_6',
            ],
            're_bladeaudiostart': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_bladeaudiostop': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_forcefielda_off': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_forcefieldb_on': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_forcefieldb_off': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_sec1blade_start': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_sec1blade_stop': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_sec2blade_start': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_sec2blade_stop': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_sec3blade_start': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_sec3blade_stop': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_sec4blade_start': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_sec4blade_stop': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'reset': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_4',
            ],
            'roundend': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_12',
            ],
            'roundstarted': [
                'Eridian_slaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.AmmoLoot.SeqEvent_RemoteEvent_0',
                'Eridian_slaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.AmmoLoot.SeqEvent_RemoteEvent_18',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_11',
            ],
            'stopmusic': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'testbubble': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.GravVacAndHazardControl_0.SeqEvent_RemoteEvent_1',
            ],
            'testkey': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective5.SeqEvent_RemoteEvent_5',
            ],
            'toggle02bubblesmoveback': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'toggle02bubblesmoveconstant': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'toggle02bubblesmoveconstantstop': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'toggle02bubblesmoveout': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'toggle02bubblesoff': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'toggle02bubbleson': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'toggledeathpitclose': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'toggledeathpitopen': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'togglelaser1': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'togglelaser2': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'togglelaser3': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'togglelowgrav': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'togglenormgrav': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'togglevacoff': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'togglevacon': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'turnlasersoff': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'turnlaserson': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ascend': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective3.SeqEvent_RemoteEvent_2',
            ],
            'bloop': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective3.SeqEvent_RemoteEvent_0',
            ],
            'debug_winround': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.Debug.SeqEvent_RemoteEvent_0',
            ],
            'debug_winwave': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.Debug.SeqEvent_RemoteEvent_1',
            ],
            'dialogs': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Mission3.SeqEvent_RemoteEvent_3',
            ],
            'ftest': [
                'Eridian_slaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'killai': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.GravVacAndHazardControl_0.SeqEvent_RemoteEvent_3',
            ],
            'loottest': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'lower': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective3.SeqEvent_RemoteEvent_3',
            ],
            're_dialog_round1plotdialog1': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_0',
            ],
            're_dialog_round1plotdialog2': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_1',
            ],
            're_dialog_round1plotdialog3': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_3',
            ],
            're_dialog_round1plotdialog3_introdialogdone': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_2',
            ],
            're_dialog_round1plotdialog4': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_4',
            ],
            're_dialog_round1plotdialog5': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_6',
            ],
            're_dialog_round1plotdialog6': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_7',
            ],
            're_gathered': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_intropart2dialogdone': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Mission1.SeqEvent_RemoteEvent_8',
            ],
            're_intro_claptrapopens': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_0',
            ],
            're_jumppad_turnoff': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_14',
            ],
            're_jumppad_turnon': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_15',
            ],
            're_keyinserted': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective5.SeqEvent_RemoteEvent_0',
            ],
            're_laser1_off': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            're_laser1_on': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_laser2_off': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_laser2_on': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            're_laser3_off': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_laser3_on': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            're_playerinmaphasneverstartedmission': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.Mission1.SeqEvent_RemoteEvent_9',
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.MissionIntro.SeqEvent_RemoteEvent_1',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_1',
            ],
            're_removerobotwaypoint': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective2.SeqEvent_RemoteEvent_1',
            ],
            're_resetwavenumber': [
                'Eridian_slaughter_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_robotdoneflash': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective2.SeqEvent_RemoteEvent_2',
            ],
            're_showsockets': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective1.SeqEvent_RemoteEvent_0',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective1.SeqEvent_RemoteEvent_10',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective1.SeqEvent_RemoteEvent_18',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective1.SeqEvent_RemoteEvent_6',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective1.SeqEvent_RemoteEvent_7',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective1.SeqEvent_RemoteEvent_8',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective1.SeqEvent_RemoteEvent_9',
            ],
            're_spawnrobot': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective2.SeqEvent_RemoteEvent_4',
            ],
            're_turnoffbrightdoor': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective5.SeqEvent_RemoteEvent_1',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective5.SeqEvent_RemoteEvent_2',
            ],
            're_turnoffjumppadbuttons': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_13',
            ],
            're_turnoffjumppads': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            're_turnonjumppadbuttons': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.DoorAndJumpPad.SeqEvent_RemoteEvent_10',
            ],
            're_turnonjumppads': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_turnonjumpad1': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_turnonjumpad2': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_turnonjumpad3': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_turnonjumpad4': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_turnonjumpad5': [
                'Eridian_Slaughter_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_zapscientists': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.GravVacAndHazardControl_0.SeqEvent_RemoteEvent_0',
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.GravVacAndHazardControl_0.SeqEvent_RemoteEvent_4',
            ],
            're_dialog_introdialogcontinued': [
                'ERIDIAN_SLAUGHTER_AUDIO.TheWorld:PersistentLevel.Main_Sequence.MissionIntro.SeqEvent_RemoteEvent_6',
            ],
            're_vaultaudiostart': [
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'roundtest': [
                'ERIDIAN_SLAUGHTER_ART.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Eridian_slaughter_Audio2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'scitesting': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective3.SeqEvent_RemoteEvent_1',
            ],
            'testbot': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.OptionalObjectives.Objective2.SeqEvent_RemoteEvent_5',
            ],
            'win': [
                'Eridian_slaughter_Scripting.TheWorld:PersistentLevel.Main_Sequence.Debug.SeqEvent_RemoteEvent_2',
            ],
        },
        'centralterminal_p': {
            'aum_kickoff': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_17',
            ],
            'activate_defense': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_75',
            ],
            'activate_lift_button': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'activiate_console': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_5',
            ],
            'agree_to_integrate': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_71',
            ],
            'all_going_to_die': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_35',
            ],
            'alma_audio': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'and_open_2': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_58',
            ],
            'and_open_again': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_49',
            ],
            'audio_disablehypfemale': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'audio_enablehypfemale': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'audio_off_cell1': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'authorization_required': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_51',
            ],
            'authorized_user': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_74',
            ],
            'bp_echo_1': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_9',
            ],
            'bp_echo_2': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_10',
            ],
            'bp_echo_3': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_11',
            ],
            'bp_echo_4': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_12',
            ],
            'bp_kickoff_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_7',
            ],
            'bp_turnin': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_13',
            ],
            'bang_on_glass': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_29',
            ],
            'blow_up_cart': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'bobs_turret': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenges.SeqEvent_RemoteEvent_8',
            ],
            'book_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_15',
            ],
            'burn1': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_0',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_25',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_6',
            ],
            'burn2': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_21',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_22',
            ],
            'burn3': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_23',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_24',
            ],
            'burn_count': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_91',
            ],
            'burning_flowers': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_15',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_2',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_5',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_9',
            ],
            'cash_used': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_3',
            ],
            'cat_combat': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Map_Combat.SeqEvent_RemoteEvent_93',
            ],
            'cat_combat_done': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_16',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_94',
            ],
            'cat_and_dog_moment': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_67',
            ],
            'clap_trapshock': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            'clap_trap_button_round2': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_1',
            ],
            'clap_trap_defend2_load': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_41',
            ],
            'clap_trap_leads_the_way': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_80',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_92',
            ],
            'clap_trap_shocking': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_73',
            ],
            'clappy_path_1': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_81',
            ],
            'claptrap_box1_load': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_35',
            ],
            'claptrap_box2_load': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_40',
            ],
            'claptrap_box3_load': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_43',
            ],
            'claptrap_greetplayers': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_50',
            ],
            'claptrap_feeling_good': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_64',
            ],
            'classy_reading': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_9',
            ],
            'clean_up_water': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_18',
            ],
            'clean_up_oil': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_21',
            ],
            'cleaning_alarm': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'clear_gas': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_7',
            ],
            'close_dialog_gate': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_1',
            ],
            'close_doors': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_28',
            ],
            'close_loop_gate': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_32',
            ],
            'close_split_combat_gate': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Map_Combat.SeqEvent_RemoteEvent_78',
            ],
            'come_to_scanner': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_40',
            ],
            'console_use_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_19',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_3',
            ],
            'continue_to_hack_dialog': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_59',
            ],
            'crush_players': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_21',
            ],
            'dahl_backup': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_4',
            ],
            'dahl_combat_load': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_14',
            ],
            'dean_rant': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_24',
            ],
            'dean_rant_2': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_11',
            ],
            'defend_1_load_anims': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_46',
            ],
            'defend_anims_load_2': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Map_Combat.SeqEvent_RemoteEvent_47',
            ],
            'defend_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_21',
            ],
            'defend_n': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_12',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_13',
            ],
            'det_complete': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_10',
            ],
            'detention_quest_completed': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_25',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_34',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_35',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_7',
            ],
            'detention_turnin': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_26',
            ],
            'do_not_open_exit': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_2',
            ],
            'don\'t_shoot': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_22',
            ],
            'door_dialog': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_53',
            ],
            'door_trigger': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_36',
            ],
            'enable_door_trigger': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_41',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_43',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_41',
            ],
            'enable_loader_dialog_trigger': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_15',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_16',
            ],
            'ep7-kickoff': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_60',
            ],
            'female_quotes': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_39',
            ],
            'fire_laser': [
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.Laser_Fire_Sequence.SeqEvent_RemoteEvent_0',
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.Laser_Fire_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'fire_laser_event': [
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.Laser_Fire_Sequence.SeqEvent_RemoteEvent_90',
            ],
            'fish_challenge': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenges.SeqEvent_RemoteEvent_2',
            ],
            'flower_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_17',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_17',
            ],
            'flower_placed_vo': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_18',
            ],
            'flowers_burnt_1': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_4',
            ],
            'flowers_burnt_2': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_11',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_7',
            ],
            'flowers_burnt_map_load': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_1',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_10',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_12',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_16',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_26',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_27',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_28',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_3',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_8',
            ],
            'follow_claptrap_load': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_34',
            ],
            'follow_claptrap_load_2': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_38',
            ],
            'follow_claptrap_load_3': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_42',
            ],
            'fuse_box_is_crap': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_65',
            ],
            'hh_kickoff': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_8',
            ],
            'heavy_snow': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'heavy_snow_test': [
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'hidewp': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_4',
            ],
            'hide_meg_as_time_is_up': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_8',
            ],
            'holojack_startpatrol': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Handsome_AI.SeqEvent_RemoteEvent_1',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Handsome_AI.SeqEvent_RemoteEvent_2',
            ],
            'hot_dog_combat': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Map_Combat.SeqEvent_RemoteEvent_95',
            ],
            'hot_dog_combat_done': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_17',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_96',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_97',
            ],
            'hot_head_completed': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_4',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_6',
            ],
            'i_think_i_got_it': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_66',
            ],
            'ice_damage_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_12',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_15',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_17',
            ],
            'ice_dean': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_52',
            ],
            'integrate': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_11',
            ],
            'integrate_action': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_72',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_72',
            ],
            'integrate_teleport': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_88',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_87',
            ],
            'jack-tassiter': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_90',
            ],
            'jack_pissed': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_29',
            ],
            'keep_lift_open': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RandD_Door_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'keep_rd_open': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RandD_Door_Sequence.SeqEvent_RemoteEvent_1',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RandD_Door_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'keep_screen_on': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_6',
            ],
            'kill_her_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_34',
            ],
            'kill_meg_active': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_3',
            ],
            'kill_meg_done': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_37',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_37',
            ],
            'kill_meg_kickoff': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_33',
            ],
            'kill_meg_turnin': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_38',
            ],
            'kindof_dangerous': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_70',
            ],
            'knock_down_trash_can': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_1',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_7',
            ],
            'laurence_audio': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'load_jacksdoorsequence': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_20',
            ],
            'loader_dialog': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_2',
            ],
            'look_at_player_1': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_78',
            ],
            'looks_great': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_10',
            ],
            'loop_back': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_31',
            ],
            'lower_innerhull_barrier': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_27',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_76',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_93',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_95',
            ],
            'maxim_audio': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'meg_has_died': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_0',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_14',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_15',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_16',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_40',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_6',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_7',
            ],
            'mission_completed': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_24',
            ],
            'move_n': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_2',
            ],
            'n_no_missions': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.No_Quests_Dialog.SeqEvent_RemoteEvent_43',
            ],
            'n_special_moves': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_30',
            ],
            'naka_hungry': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_45',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_39',
            ],
            'no_combat': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_15',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_16',
            ],
            'no_ice_damage_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_13',
            ],
            'no_mission_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_42',
            ],
            'noooo': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_19',
            ],
            'oil_spill': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_20',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_28',
            ],
            'on_cc_turn_in': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_30',
            ],
            'on_load_defend_snow_storm': [
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_91',
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_92',
                'CentralTerminal_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_91',
            ],
            'on_ready_to_turnin': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_33',
            ],
            'open_cash': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_2',
            ],
            'open_cell_doors': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_1',
            ],
            'open_clap_locker_load': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_18',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_86',
            ],
            'open_clappy_locker_door': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_89',
            ],
            'open_closet_door': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_1',
            ],
            'open_deans_locker': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_2',
            ],
            'open_final_doors': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'open_front_door': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_27',
            ],
            'open_gun_shop': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_77',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_78',
            ],
            'open_jack_doors': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'open_locker_door': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_28',
            ],
            'open_office_door': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_5',
            ],
            'open_panel_3_load': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_63',
            ],
            'open_rd': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.RandD_Door_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'open_repair_door': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_19',
            ],
            'open_sec_doors': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_9',
            ],
            'open_sec_no_combat': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_11',
            ],
            'open_security_doors': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_0',
            ],
            'open_shop': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_25',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_43',
            ],
            'open_shop_door': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_32',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_26',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_29',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_32',
            ],
            'open_top_door': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'open_trash': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_27',
            ],
            'open_trash_compactor': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_28',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_36',
            ],
            'open_trash_exit': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_5',
            ],
            'open_laser_gate': [
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.Laser_Fire_Sequence.SeqEvent_RemoteEvent_91',
            ],
            'pj_kickoff': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_13',
            ],
            'pj_plan': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_14',
            ],
            'pj_turnin': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Paint_Job.SeqEvent_RemoteEvent_20',
            ],
            'paper_shrink': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_13',
            ],
            'papers_3': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_0',
            ],
            'pissed_off_about_trash': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_23',
            ],
            'pissed_off_about_water': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_26',
            ],
            're_alarm': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_cc_kickoff': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_4',
            ],
            're_claptrap_button_round3': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_22',
            ],
            're_claptrap_dead_state': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_29',
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            're_claptrap_move_to_door': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_16',
            ],
            're_claptrap_open_round2': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_79',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_18',
            ],
            're_claptrap_pushbuttons': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_7',
            ],
            're_combat_1': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Map_Combat.SeqEvent_RemoteEvent_0',
            ],
            're_fall_down': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_14',
            ],
            're_lilith_gladiator_arirlock_vo': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Inner_Hull.SeqEvent_RemoteEvent_2',
            ],
            're_move_to_box_1': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_25',
            ],
            're_open_vent': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_0',
            ],
            're_snow': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_56',
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            're_start_trash_compactor': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_12',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_13',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_18',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_4',
            ],
            're_stop_loop_2': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_26',
            ],
            're_stop_snow': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'CentralTerminal_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'random_dean_end_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_93',
            ],
            'reset_trash_compactor': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_10',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_17',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_19',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_20',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_22',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_24',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_30',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_31',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_42',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_44',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_45',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_9',
            ],
            'roomba1_found': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_34',
            ],
            'roomba_1_loop': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_15',
            ],
            'roomba_2_found': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_45',
            ],
            'roomba_2_loop': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_19',
            ],
            'roomba_3_loop': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_22',
            ],
            'roomba_loop': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_4',
            ],
            'rosie_no_missions': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.No_Quests_Dialog.SeqEvent_RemoteEvent_44',
            ],
            'scan_books': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_1',
            ],
            'scanner': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_54',
            ],
            'sendnaytoperch_pushbuttonmission': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_44',
            ],
            'sequence_3': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_62',
            ],
            'shoot_console': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_38',
            ],
            'shoot_console_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_20',
            ],
            'snow_tornado': [
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'spawn_dahl_pranksters': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_2',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_3',
            ],
            'spawn_guards': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_40',
            ],
            'spawn_meg': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_23',
            ],
            'startsnowevent': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_15',
            ],
            'start_anims': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_16',
            ],
            'start_roomba_1': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_24',
            ],
            'start_roomba_2': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_27',
            ],
            'start_roomba_3': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_29',
            ],
            'start_roomba_combat_1': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cleaning_Side_Quest_Combat.SeqEvent_RemoteEvent_8',
            ],
            'start_roomba_combat_2': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cleaning_Side_Quest_Combat.SeqEvent_RemoteEvent_10',
            ],
            'start_roomba_combat_3': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Cleaning_Side_Quest_Combat.SeqEvent_RemoteEvent_12',
            ],
            'steam': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_26',
            ],
            'stop_anim_loop': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_33',
            ],
            'stop_loop_1': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_23',
            ],
            'stop_roomba3_track': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_11',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_12',
            ],
            'stop_roomba_1_track': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_25',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_5',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_6',
            ],
            'stop_roomba_2_track': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_10',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_9',
            ],
            'tv_fallen': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_6',
            ],
            'tv_falls': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_5',
            ],
            'talk_to_claptrap_load': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_33',
            ],
            'teleport_clap_1': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_36',
            ],
            'teleport_dean': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_14',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_50',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_51',
            ],
            'thank_you': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_6',
            ],
            'toggle_pp': [
                'CentralTerminal_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_77',
            ],
            'trash_can_down_frame': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_3',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_8',
            ],
            'trash_completed': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_19',
            ],
            'trash_falls': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Kill_Meg.SeqEvent_RemoteEvent_11',
            ],
            'trash_opened': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_1',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_17',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_18',
            ],
            'turn_off_impact': [
                'CentralTerminal_FX.TheWorld:PersistentLevel.Main_Sequence.Laser_Fire_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'turn_off_scanner': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_61',
            ],
            'turn_off_shock': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_31',
            ],
            'typing_load_1': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_45',
            ],
            'unhide_frozen_dean': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_7',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_9',
            ],
            'unhide_ice_man': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_0',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_5',
            ],
            'unhide_mesh_books': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_0',
            ],
            'unlock_level_challenge': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenges.SeqEvent_RemoteEvent_0',
            ],
            'upload_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_24',
            ],
            'upload_message': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_23',
            ],
            'use_console_dialog': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_18',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_8',
            ],
            'user_is_cat': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_68',
            ],
            'user_is_dog': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_69',
            ],
            'vo_cont.': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_13',
            ],
            'vo_turnin': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_11',
            ],
            'vent2_completed': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_14',
            ],
            'vent2_open': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_8',
            ],
            'voice_over_active': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'voice_over_complete': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'water_sequence': [
                'CentralTerminal_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Cleanliness_Uprising.SeqEvent_RemoteEvent_16',
            ],
            'wrong_door_combat': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Map_Combat.SeqEvent_RemoteEvent_77',
            ],
            'wrong_door_combat_2': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Map_Combat.SeqEvent_RemoteEvent_79',
            ],
            're_doorclosedfanfare': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.SeqEvent_RemoteEvent_0',
            ],
            'restart_rant': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Hot_Head_Sidequest.SeqEvent_RemoteEvent_95',
            ],
            'station_in_one_piece': [
                'CentralTerminal_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Plot_HeliosFoothold.Dialog.SeqEvent_RemoteEvent_91',
            ],
            'turn_off_glow_trigger': [
                'CentralTerminal_Missions.TheWorld:PersistentLevel.Main_Sequence.Detention_Sidequest.SeqEvent_RemoteEvent_39',
            ],
        },
        'jacksoffice_p': {
            'aum_kickoff': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.An_Urgent_Message.SeqEvent_RemoteEvent_0',
            ],
            'activatetalkjacktrigger': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_80.SeqEvent_RemoteEvent_53',
            ],
            'audio_controlpanel_exposed': [
                'JacksOffice_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'JacksOffice_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'audio_startpainting': [
                'JacksOffice_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'bp_kickoff_dialog': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_7',
            ],
            'bp_turnin': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Boarding_Party.SeqEvent_RemoteEvent_13',
            ],
            'body_double_echo_1': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Body_Double_Echos.SeqEvent_RemoteEvent_0',
            ],
            'body_double_echo_2': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Body_Double_Echos.SeqEvent_RemoteEvent_1',
            ],
            'body_double_echo_3': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Body_Double_Echos.SeqEvent_RemoteEvent_2',
            ],
            'body_double_echo_4': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Body_Double_Echos.SeqEvent_RemoteEvent_3',
            ],
            'buttonready': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_160.SeqEvent_RemoteEvent_13',
            ],
            'change_scalar_value': [
                'JacksOffice_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'clap_trap_painting_finished': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_0',
                'JacksOffice_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'claptrap_accepts_paint': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_13',
            ],
            'close_danceloop_gate': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_12',
            ],
            'deactivatetalkjacktrigger': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_80.SeqEvent_RemoteEvent_52',
            ],
            'dialog_1': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_40',
            ],
            'dialog_tree_1': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Body_Double_Echos.SeqEvent_RemoteEvent_4',
            ],
            'dialog_tree_2': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Body_Double_Echos.SeqEvent_RemoteEvent_5',
            ],
            'dialog_tree_3': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Body_Double_Echos.SeqEvent_RemoteEvent_6',
            ],
            'dialog_tree_4': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Body_Double_Echos.SeqEvent_RemoteEvent_7',
            ],
            'fire_laser': [
                'JacksOffice_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'go': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'go_to_randd_office_door': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'hh_kickoff': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Hot_Head.SeqEvent_RemoteEvent_0',
            ],
            'hold_out_hand': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_35',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_37',
            ],
            'hot_head_turn_in': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Hot_Head.SeqEvent_RemoteEvent_1',
            ],
            'jack_goes_into_office': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jack_Door.SeqEvent_RemoteEvent_8',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'jack_lines_after_fast_travel': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Foot_Hold_Plot.SeqEvent_RemoteEvent_1',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'jack_reply': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_16',
            ],
            'jack_hates_it': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_38',
            ],
            'keep_painting': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_39',
                'JacksOffice_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'JacksOffice_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'level_challenge_burn': [
                'JacksOffice_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenge.SeqEvent_RemoteEvent_2',
            ],
            'loot_chest_dialog': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Foot_Hold_Plot.SeqEvent_RemoteEvent_14',
            ],
            'move_to_wall': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_5',
            ],
            'on_turn_in': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Foot_Hold_Plot.SeqEvent_RemoteEvent_0',
            ],
            'open_office_door': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Jack_Door.SeqEvent_RemoteEvent_7',
            ],
            'paint_loop': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_26',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_6',
            ],
            'play_jack_dialog': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Foot_Hold_Plot.SeqEvent_RemoteEvent_3',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'player_gives_paint': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_15',
            ],
            're_airlockfinished': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_320.SeqEvent_RemoteEvent_7',
            ],
            're_breakawayfromjack': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_370.SeqEvent_RemoteEvent_3',
            ],
            're_buttonagain': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_clap': [
                'JacksOffice_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_closeairlock': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_170.SeqEvent_RemoteEvent_4',
            ],
            're_exposebutton': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_flipcontrolpanel': [
                'JacksOffice_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'JacksOffice_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_give_loop_stop': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_3',
            ],
            're_give_paint': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_2',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_36',
            ],
            're_jackdont': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_270.SeqEvent_RemoteEvent_11',
            ],
            're_makejacksit': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_moveliltoroland': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_openshutters': [
                'JacksOffice_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_returntospots': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_rolandinplaceformoxxiline': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_370.SeqEvent_RemoteEvent_8',
            ],
            're_scisuprise': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_180.SeqEvent_RemoteEvent_0',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_190.SeqEvent_RemoteEvent_0',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_200.SeqEvent_RemoteEvent_0',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_210.SeqEvent_RemoteEvent_0',
            ],
            're_scientistsdead': [
                'JacksOffice_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_startairlockseq': [
                'JacksOffice_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_startrolnlilmoving': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_start_painting': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_4',
            ],
            're_startup': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_1',
            ],
            're_suckedout': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_280.SeqEvent_RemoteEvent_9',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_290.SeqEvent_RemoteEvent_9',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_300.SeqEvent_RemoteEvent_9',
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_MissionVO.SS_310.SeqEvent_RemoteEvent_9',
            ],
            'restart_dance_loop': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_11',
            ],
            'set_value_to_1': [
                'JacksOffice_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'JacksOffice_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'test': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'trigger_give_paint': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Mementos.SeqEvent_RemoteEvent_7',
            ],
            'turn_off_impact': [
                'JacksOffice_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'update_lc_bookworm': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenge.SeqEvent_RemoteEvent_0',
            ],
            'update_lc_firey_filer': [
                'JacksOffice_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenge.SeqEvent_RemoteEvent_1',
            ],
            'vo_kick_off': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_40',
            ],
            'vo_player_response': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_38',
            ],
            'vo_turnin': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.Voice_Over.SeqEvent_RemoteEvent_1',
            ],
            'perchtest': [
                'JacksOffice_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
        },
        'laser_p': {
            'containerspeed_fast': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_16',
            ],
            'containerspeed_reset': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_7',
            ],
            'containerspeed_slow': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_1',
            ],
            'containerspeed_slow_gradual': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_5',
            ],
            'convey_lt_phys_turnoff': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_12',
            ],
            'convey_lt_phys_turnon': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_11',
            ],
            'convey_rt_phys_turnoff': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.SeqEvent_RemoteEvent_0',
            ],
            'convey_rt_phys_turnon': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.SeqEvent_RemoteEvent_11',
            ],
            'destroyloaders': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.SeqEvent_RemoteEvent_10',
            ],
            'enablepartylight': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqEvent_RemoteEvent_1',
            ],
            'firelasernow': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'gsystemgothit': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.SeqEvent_RemoteEvent_4',
            ],
            'guidancesystembroken': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Fail_Condition.SeqEvent_RemoteEvent_10',
            ],
            'power_play_counter': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenges.SeqEvent_RemoteEvent_4',
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenges.SeqEvent_RemoteEvent_5',
            ],
            're_showeye': [
                'Laser_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_test': [
                'Laser_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_reddead_firstredshirtdied': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_1',
            ],
            'redshirtrunner_spawned': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_9',
            ],
            'sendbike': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'turn_off_level_challenge_trigger': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Clip_Firing.SeqEvent_RemoteEvent_4',
            ],
            'turn_on_level_challenge_trigger': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Clip_Firing.SeqEvent_RemoteEvent_2',
            ],
            'dialog_drainingstarted': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_3',
            ],
            'go2_mooncon': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_activatefasttravel': [
                'Laser_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_active_explodersmission': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.Fix_Loader.SeqEvent_RemoteEvent_5',
            ],
            're_allpowerlineson': [
                'Laser_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.PowerLines.SeqEvent_RemoteEvent_0',
            ],
            're_bottomcomat_lockothers': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PowerCoreRoom.SeqEvent_RemoteEvent_0',
            ],
            're_bottomcombat_turnoffallpoppoints': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PowerCoreRoom.SeqEvent_RemoteEvent_4',
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PowerCoreRoom.SeqEvent_RemoteEvent_5',
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PowerCoreRoom.SeqEvent_RemoteEvent_6',
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.PowerCoreRoom.SeqEvent_RemoteEvent_7',
            ],
            're_clearclip': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Clip_Firing.SeqEvent_RemoteEvent_7',
            ],
            're_complete_explodersmission': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.Fix_Loader.SeqEvent_RemoteEvent_6',
            ],
            're_criticalwarninglight_off': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_0',
            ],
            're_criticalwarninglight_on': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_3',
            ],
            're_deactivatefasttravel': [
                'Laser_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_debughideshutters': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.ActivateCommandStation.SeqEvent_RemoteEvent_1',
            ],
            're_dia_reddead_echo1': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_10',
            ],
            're_dia_reddead_echo2': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_3',
            ],
            're_dia_reddead_echo3': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Red_Then_Dead.SeqEvent_RemoteEvent_5',
            ],
            're_dialog_botbeingdamaged': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_9',
            ],
            're_dialog_dahlresponse1': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_5',
            ],
            're_dialog_dahlresponse2': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_4',
            ],
            're_dialog_ffbroughtdownsuccess': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_0',
            ],
            're_dialog_ffdialog': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.FusionCore01.SeqEvent_RemoteEvent_0',
            ],
            're_dialog_guybangingoncontainer': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.SeqEvent_RemoteEvent_3',
            ],
            're_disablehyperionforcefield': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.ForceField.SeqEvent_RemoteEvent_2',
            ],
            're_enablebreadcrumbareawaypoints': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.FusionCore02.SeqEvent_RemoteEvent_0',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.FusionCore03.SeqEvent_RemoteEvent_0',
            ],
            're_enablejackden': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.SeqEvent_RemoteEvent_3',
            ],
            're_firelasernow': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_forcecliploading': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.ClipLoading.SeqEvent_RemoteEvent_13',
            ],
            're_getanothercontainer': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqEvent_RemoteEvent_2',
            ],
            're_gunrelax': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Clip_Firing.SeqEvent_RemoteEvent_0',
            ],
            're_guynoticesgoodies': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqEvent_RemoteEvent_3',
            ],
            're_ini_stop': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SendGuyToShutdown.SeqEvent_RemoteEvent_5',
            ],
            're_int_pawnsarrivedafewtimes': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SendGuyToShutdown.SeqEvent_RemoteEvent_0',
            ],
            're_inifirecomputer': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Clip_Firing.SeqEvent_RemoteEvent_9',
            ],
            're_jacknpc_turnoffscriptednarrative': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.ActivateCommandStation.SeqEvent_RemoteEvent_5',
            ],
            're_jackopensdoor': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.ActivateCommandStation.SeqEvent_RemoteEvent_0',
            ],
            're_jackspawn_atpointa': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.ActivateCommandStation.SeqEvent_RemoteEvent_6',
            ],
            're_jackspawned': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.JackScripting_Common.SeqEvent_RemoteEvent_14',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.JackScripting_Common.SeqEvent_RemoteEvent_2',
            ],
            're_jack_setscriptednarrative': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.JackScripting_Common.SeqEvent_RemoteEvent_9',
            ],
            're_jack_unsetscriptednarrative': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.JackScripting_Common.SeqEvent_RemoteEvent_5',
            ],
            're_kickoff_reddead_playrestofdialog': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_2',
            ],
            're_kickoff_redthendead': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_11',
            ],
            're_ll_spawnpowersuit': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_LockAndLoad.SeqEvent_RemoteEvent_0',
            ],
            're_ll_turnonstage1': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_LockAndLoad.SeqEvent_RemoteEvent_5',
            ],
            're_ll_turnonstage2': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_LockAndLoad.SeqEvent_RemoteEvent_7',
            ],
            're_ll_turnonstage3': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_LockAndLoad.SeqEvent_RemoteEvent_8',
            ],
            're_laserexplosion_lightblind': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_11',
            ],
            're_laserexplosion_sidewindowhit': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_13',
            ],
            're_lasermission_enemyturnoffpowerdrain': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_1',
            ],
            're_lasermomentshake_constant': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_lasermomentshake_explosion': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_lasermomentshake_stop': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_laserpchallenge_powersuitdestroyed': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenges.SeqEvent_RemoteEvent_2',
            ],
            're_laserpchallenge_updatelaserchallenge': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenges.SeqEvent_RemoteEvent_1',
            ],
            're_levelchallenge_alittlehelp': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Level_Challenges.SeqEvent_RemoteEvent_3',
            ],
            're_loaderdestroyed': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.SeqEvent_RemoteEvent_16',
            ],
            're_loadergothit': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.SeqEvent_RemoteEvent_12',
            ],
            're_loading_pausemainfloorcombat': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.LoadingStationCombat.SeqEvent_RemoteEvent_2',
            ],
            're_lockandload_startcombat': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_LockAndLoad.SeqEvent_RemoteEvent_17',
            ],
            're_lockload_kickoff': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.SeqEvent_RemoteEvent_11',
            ],
            're_makepresent': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_2',
            ],
            're_makevanish': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_3',
            ],
            're_missiondone_deleteall': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.LoaderRackMatinees.SeqEvent_RemoteEvent_0',
            ],
            're_missionfailed': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.SeqEvent_RemoteEvent_17',
            ],
            're_missionstate_beforeleftrightpowercore': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_2',
            ],
            're_moonshotdonefiring': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.LockAndLoad.SeqEvent_RemoteEvent_2',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Success_Condition.SeqEvent_RemoteEvent_2',
            ],
            're_moonshotloading_allspawnsoff': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.SeqEvent_RemoteEvent_4',
            ],
            're_offjacksmoke': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_onload_digistructdoor': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqEvent_RemoteEvent_6',
            ],
            're_onload_setlaserdestroyedstate': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.OnLoadHandling.SeqEvent_RemoteEvent_0',
            ],
            're_openuprightpath': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Doors.SeqEvent_RemoteEvent_0',
            ],
            're_pausedrainingpower': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_8',
            ],
            're_pauseencounter': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_11',
            ],
            're_playernearby': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_11',
            ],
            're_popintoposition01': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.INI.SeqEvent_RemoteEvent_6',
            ],
            're_popintoposition02': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqEvent_RemoteEvent_7',
            ],
            're_poppoint_eastsidecombat_hidedoor': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PowerDownGenCombat.SeqEvent_RemoteEvent_0',
            ],
            're_postdialog': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_10',
            ],
            're_postintrodialogdone': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_5',
            ],
            're_powerdownfusionpipes': [
                'Laser_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_powerupfusionpipes': [
                'Laser_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_protectloaderspawned': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_23',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_25',
            ],
            're_reddead_gotofirstpoint': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_12',
            ],
            're_reddead_gotosecondpoint': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_8',
            ],
            're_reddead_gotothirdpoint': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_7',
            ],
            're_releasefromcharging': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_2',
            ],
            're_removeallpowerwaypoints': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.FusionCoreCommon.SeqEvent_RemoteEvent_3',
            ],
            're_resetmission': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThingsBoomCombat.SeqEvent_RemoteEvent_24',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_10',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_12',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_5',
            ],
            're_resetorder': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.ClipLoading.SeqEvent_RemoteEvent_10',
            ],
            're_resettargetdevicelocation': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.INI.SeqEvent_RemoteEvent_9',
            ],
            're_resumefeeding': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_6',
            ],
            're_sendtospotawayfromplayer': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_20',
            ],
            're_sendtostation': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_6',
            ],
            're_sendtostation_facetarget': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_3',
            ],
            're_shiphitbymoonshot': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.IdleShipFloating.SeqEvent_RemoteEvent_0',
            ],
            're_shipshidden': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.IdleShipFloating.SeqEvent_RemoteEvent_1',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Clip_Firing.SeqEvent_RemoteEvent_1',
            ],
            're_shuttersopen': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.ActivateCommandStation.SeqEvent_RemoteEvent_4',
            ],
            're_slowdowntimer': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_0',
            ],
            're_slowtest': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_0',
            ],
            're_speeduptimer': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_1',
            ],
            're_startblackholesequence': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_startdrainingpower': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_6',
            ],
            're_startgravity': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.FlyingDebris.SeqEvent_RemoteEvent_1',
            ],
            're_startguysgoingforbutton': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_13',
            ],
            're_startlaserglowies': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_12',
            ],
            're_startlaserloop': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_stopdraincombat': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_7',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_9',
            ],
            're_stopgravdebris': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.FlyingDebris.SeqEvent_RemoteEvent_3',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.FlyingDebris.SeqEvent_RemoteEvent_4',
            ],
            're_stopguysgoingforbutton': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_2',
            ],
            're_stoplaseridle': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_6',
            ],
            're_stopshipidlemovement': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.IdleShipFloating.SeqEvent_RemoteEvent_5',
            ],
            're_ttm_spawnpowersuit': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_ToTheMoon_0.SeqEvent_RemoteEvent_0',
            ],
            're_ttm_turnonstage1': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_ToTheMoon_0.SeqEvent_RemoteEvent_5',
            ],
            're_ttm_turnonstage2': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_ToTheMoon_0.SeqEvent_RemoteEvent_7',
            ],
            're_ttm_turnonstage3': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_ToTheMoon_0.SeqEvent_RemoteEvent_8',
            ],
            're_targetdevicespawned': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqEvent_RemoteEvent_0',
            ],
            're_theendmission_kickoff': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.SeqEvent_RemoteEvent_0',
            ],
            're_thingsboom_dialogresponse1': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.DialogResponse.SeqEvent_RemoteEvent_27',
            ],
            're_thingsboom_dialogresponse2': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.DialogResponse.SeqEvent_RemoteEvent_29',
            ],
            're_thingsboom_dialogresponse3': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.DialogResponse.SeqEvent_RemoteEvent_24',
            ],
            're_thingsboom_dialog_kickoff': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_7',
            ],
            're_thingsboom_dialog_turnin': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_18',
            ],
            're_thingsboom_downloadcombat_start': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThingsBoomCombat.SeqEvent_RemoteEvent_20',
            ],
            're_thingsboom_downloadcombat_stop': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThingsBoomCombat.SeqEvent_RemoteEvent_23',
            ],
            're_thingsboom_downloadstarting': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_14',
            ],
            're_thingsboom_downloaderstart': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_13',
            ],
            're_thingsboom_downloaderstop': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_19',
            ],
            're_thingsboom_feelpowerdialog': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_17',
            ],
            're_thingsboom_removewaypoint': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_16',
            ],
            're_thingsboom_sayloaderattackdialog': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.DialogResponse.SeqEvent_RemoteEvent_26',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.DialogResponse.SeqEvent_RemoteEvent_28',
            ],
            're_thingsboom_turnoffcombatdens': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThingsBoomCombat.SeqEvent_RemoteEvent_19',
            ],
            're_thingsboom_turnoncombatdens': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThingsBoomCombat.SeqEvent_RemoteEvent_22',
            ],
            're_thingsboom_turnonupperden': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThingsBoomCombat.SeqEvent_RemoteEvent_13',
            ],
            're_tothemoon_attachtoconsolecontainer': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Attaching.SeqEvent_RemoteEvent_2',
            ],
            're_tothemoon_attachtodefendcontainer': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Attaching.SeqEvent_RemoteEvent_1',
            ],
            're_tothemoon_dialog_kickoff': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.SeqEvent_RemoteEvent_19',
            ],
            're_tothemoon_failsafe_guyentered': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqEvent_RemoteEvent_4',
            ],
            're_tothemoon_startcombat': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.MoonshotLoading.Combat_ToTheMoon_0.SeqEvent_RemoteEvent_3',
            ],
            're_tothemoon_turnin': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Success_Condition.SeqEvent_RemoteEvent_8',
            ],
            're_turnin_readdead': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_6',
            ],
            're_turnoffeastsidegencombat': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EastSideWingCombat.SeqEvent_RemoteEvent_1',
            ],
            're_turnoffgoodies': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ToTheMoon.Setup_Scripting.SeqEvent_RemoteEvent_5',
            ],
            're_turnoffhallwaydens': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ThingsBoomCombat.SeqEvent_RemoteEvent_21',
            ],
            're_turnoffjusttraveltolaser': [
                'Laser_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_turnofftraveltolaser': [
                'Laser_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_turnonblockervisuals': [
                'Laser_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_turnoneastsidegencombat': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.EastSideWingCombat.SeqEvent_RemoteEvent_2',
            ],
            're_turnonlaserdestroyedvisual': [
                'Laser_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_turnonlevelcombats': [
                'Laser_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_unpauseencounter': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_10',
            ],
            're_dialog_gotomainreactor': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.FusionCoreCommon.SeqEvent_RemoteEvent_2',
            ],
            're_dialog_moxpowernodereminder': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.FusionCoreCommon.SeqEvent_RemoteEvent_1',
            ],
            're_dialog_solmadeittoreactor': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SendGuyToShutdown.SeqEvent_RemoteEvent_6',
            ],
            're_int_searchagain': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SendGuyToShutdown.SeqEvent_RemoteEvent_2',
            ],
            're_introdialogdone': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.TimedCombat.SeqEvent_RemoteEvent_4',
            ],
            're_powerlines_turnoffset1': [
                'Laser_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.PowerLines.SeqEvent_RemoteEvent_9',
            ],
            're_powerlines_turnoffset2': [
                'Laser_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.PowerLines.SeqEvent_RemoteEvent_6',
            ],
            're_powerlines_turnoffset3': [
                'Laser_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.PowerLines.SeqEvent_RemoteEvent_5',
            ],
            're_powerlines_turnoffset4': [
                'Laser_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.PowerLines.SeqEvent_RemoteEvent_3',
            ],
            're_powerlines_turnonset2': [
                'Laser_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.PowerLines.SeqEvent_RemoteEvent_7',
            ],
            're_powerlines_turnonset3': [
                'Laser_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.PowerLines.SeqEvent_RemoteEvent_4',
            ],
            're_powerlines_turnonset4': [
                'Laser_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.PowerCells.PowerLines.SeqEvent_RemoteEvent_2',
            ],
            're_reddead_start2ndrsdialog': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_13',
            ],
            're_redshirt_pawninsaferoom': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_14',
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_15',
            ],
            're_redshirt_resetoutbutton': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.RedShirt.SeqEvent_RemoteEvent_0',
            ],
            're_testing_teststart': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_4',
            ],
            're_thingsboom_dialog_followloader': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.ThingsThatGoBoom.SeqEvent_RemoteEvent_8',
            ],
            're_tothemoon_pausefeeding': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.MoonshotCannon.Conveyor.SeqEvent_RemoteEvent_10',
            ],
            're_turnoffsparkeffects': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_2',
            ],
            'test_laserdestruct': [
                'Laser_Mission.TheWorld:PersistentLevel.Main_Sequence.PlotMission.LaserExplosion.SeqEvent_RemoteEvent_8',
            ],
        },
        'meriff_p': {
            'debugspawnais': [
                'Meriff_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Meriff_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Meriff_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'dialog_jackbookcase': [
                'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'dialog_jackslotmachine': [
                'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'disablepasquiggles': [
                'Meriff_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'enablepasquiggles': [
                'Meriff_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'm_chp04_liftatlowerpoint': [
                'Meriff_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'm_chp04_merriftitlecardcomplete': [
                'Meriff_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'm_chp04_trggermerriftitlecard': [
                'Meriff_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'm_cph04_forcefieldfade': [
                'Meriff_M_Chp4.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            'slotmachine_startechomat': [
                'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'wipingslate_pullbookmat': [
                'Meriff_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
        },
        'ma_motherboard_p': {
            '1sttrophyalreadypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            '1sttrophynotpickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            '1sttrophypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            '2ndtrophyalreadypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            '2ndtrophynotpickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            '2ndtrophypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            '3rdtrophyalreadypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            '3rdtrophynotpickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            '3rdtrophypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            '4thtrophyalreadypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            '4thtrophynotpickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            '4thtrophypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            '5thtrophyalreadypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            '5thtrophynotpickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            '5thtrophypickedup': [
                'Ma_Motherboard_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'audio_dataon': [
                'Ma_Motherboard_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'audio_dataonfirst': [
                'Ma_Motherboard_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'damageddatastream_off': [
                'Ma_Motherboard_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'damageddatastream_on': [
                'Ma_Motherboard_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'deletionfieldai_wounded': [
                'Ma_Motherboard_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_5',
            ],
            'securitychkpoint_disabled': [
                'Ma_Motherboard_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'securitychkpoint_enabled': [
                'Ma_Motherboard_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'securitygate_off': [
                'Ma_Motherboard_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'securitygate_on': [
                'Ma_Motherboard_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'virusai_changebehavior': [
                'Ma_Motherboard_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_4',
            ],
            'virusai_dmgwall': [
                'Ma_Motherboard_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_3',
            ],
            'virushitmissiondeletionfield': [
                'Ma_Motherboard_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_1',
            ],
        },
        'ma_nexus_p': {
            'acceptmissionnag': [
                'Ma_Nexus_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'ambientmadtrapshow': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.QuarantineCharacterDisplay.SeqEvent_RemoteEvent_7',
            ],
            'breaklensleanloop': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Iris.SeqEvent_RemoteEvent_3',
            ],
            'bucketoilfill': [
                'Ma_Nexus_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'crusherdooropen': [
                'Ma_Nexus_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'deflatedresponse': [
                'Ma_Nexus_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'destroyhackbot2': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03.PostLeftCluster.SeqEvent_RemoteEvent_0',
            ],
            'destroymaddialogactor': [
                'Ma_Nexus_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'destroyshadowdialogactor': [
                'Ma_Nexus_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'destroyedhackbot2': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'disablebugtrashspawners': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_28',
            ],
            'disablelasers': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_3',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_6',
            ],
            'disabletownbugs': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.TownSpyAndAdBugs.SeqEvent_RemoteEvent_0',
            ],
            'egotrophysgiven': [
                'Ma_Nexus_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'enablebugtrashspawners': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_5',
            ],
            'enablefirstweakpoints': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_1',
            ],
            'enablelasers': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_23',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_4',
            ],
            'enablesubplatform': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter05.SeqEvent_RemoteEvent_4',
            ],
            'enabletownbugs': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.TownSpyAndAdBugs.SeqEvent_RemoteEvent_1',
            ],
            'endquaropenloop': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'gjambientlensleanforcestart': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Iris.SeqEvent_RemoteEvent_5',
            ],
            'gjambientlensleanstart': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Iris.SeqEvent_RemoteEvent_15',
            ],
            'hackbug1destroy': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'hackbug1destroypulse': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03.PostLeftCluster.SeqEvent_RemoteEvent_9',
            ],
            'hidehsource': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_9',
            ],
            'hidemadtrap': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.QuarantineCharacterDisplay.SeqEvent_RemoteEvent_5',
            ],
            'hideshadowtrap': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.QuarantineCharacterDisplay.SeqEvent_RemoteEvent_6',
            ],
            'jackleanloopstart': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Iris.SeqEvent_RemoteEvent_2',
            ],
            'jackleavelens': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Iris.SeqEvent_RemoteEvent_6',
            ],
            'lasertrapended': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_10',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_24',
            ],
            'lensloopbroken': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Iris.SeqEvent_RemoteEvent_1',
            ],
            'lensopened': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_1',
            ],
            'lowershadowplatform': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_2',
            ],
            'metatrapfasttraveledin': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_2',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_14',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_18',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_2',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_21',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_26',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_8',
            ],
            'metatrapfasttraveledout': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_11',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_8',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_13',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_17',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_19',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_20',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_27',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_7',
            ],
            'metatraptitlecard_ended': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_6',
            ],
            'metatraptitlecard_start': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'openlens': [
                'Ma_Nexus_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Iris.SeqEvent_RemoteEvent_0',
            ],
            'openquarantinedoors': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Quarantine.SeqEvent_RemoteEvent_7',
            ],
            'opensubleveltransition': [
                'Ma_Nexus_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'player0enteredvolume': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.IsInVolume.SeqEvent_RemoteEvent_5',
            ],
            'player0leftvolume': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.IsInVolume.SeqEvent_RemoteEvent_7',
            ],
            'player1enteredvolume': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.IsInVolume.SeqEvent_RemoteEvent_6',
            ],
            'player1leftvolume': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.IsInVolume.SeqEvent_RemoteEvent_8',
            ],
            'player2enteredvolume': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.IsInVolume.SeqEvent_RemoteEvent_4',
            ],
            'player2leftvolume': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.IsInVolume.SeqEvent_RemoteEvent_10',
            ],
            'player3enteredvolume': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.IsInVolume.SeqEvent_RemoteEvent_3',
            ],
            'player3leftvolume': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.IsInVolume.SeqEvent_RemoteEvent_9',
            ],
            'powernodedestroyed': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_0',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.EnableWeakPoints.SeqEvent_RemoteEvent_0',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.EnableWeakPoints_0.SeqEvent_RemoteEvent_0',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.EnableWeakPoints_3.SeqEvent_RemoteEvent_0',
            ],
            'qc_lowerposition': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'qc_openquaratine': [
                'Ma_Nexus_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'qc_raiseposition': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'qc_spawnshadow': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_8',
            ],
            'quardisablepanel': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_1',
            ],
            'quarenablepanel': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_0',
            ],
            'quarfogsettothin': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_7',
            ],
            'quarmadtrapappear': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.QuarantineCharacterDisplay.SeqEvent_RemoteEvent_2',
            ],
            'quarmadtrapdisappear': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.QuarantineCharacterDisplay.SeqEvent_RemoteEvent_3',
            ],
            'quaropenloopended': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_3',
            ],
            'raiseplatforms': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_9',
            ],
            'scancompleteenabletrap': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_25',
            ],
            'setbacktoblue': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_13',
            ],
            'setbacktored': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_0',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_10',
            ],
            'setcrusherdoorshut': [
                'Ma_Nexus_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'setquarfogthin': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'shadowopenportal': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_6',
            ],
            'shadowtrapreleased': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter04.SeqEvent_RemoteEvent_4',
            ],
            'shadowtraptitlecard_ended': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03.PostLeftCluster.SeqEvent_RemoteEvent_4',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Iris.SeqEvent_RemoteEvent_4',
            ],
            'shadowtraptitlecard_start': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'showmadtrapfade': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.QuarantineCharacterDisplay.SeqEvent_RemoteEvent_4',
            ],
            'showshadowtrap': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.QuarantineCharacterDisplay.SeqEvent_RemoteEvent_0',
            ],
            'showshadowtrapfade': [
                'Ma_Nexus_Cinematics.TheWorld:PersistentLevel.Main_Sequence.QuarantineCharacterDisplay.SeqEvent_RemoteEvent_1',
            ],
            'showvortexcubes': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.SubVortex.SeqEvent_RemoteEvent_6',
            ],
            'spywareproximity': [
                'Ma_Nexus_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'subleveltransitionopened': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter05.SeqEvent_RemoteEvent_23',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter05.SeqEvent_RemoteEvent_8',
            ],
            'sysadmin_startambientanim': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_7',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_9',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SettingSysAdminScreenColour.SeqEvent_RemoteEvent_4',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Sysadmin.SeqEvent_RemoteEvent_11',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Sysadmin.SeqEvent_RemoteEvent_4',
            ],
            'sysadmin_stopambientanim': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Sysadmin.SeqEvent_RemoteEvent_0',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Sysadmin.SeqEvent_RemoteEvent_3',
            ],
            'sysadmin_talkloop': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Sysadmin.SeqEvent_RemoteEvent_2',
            ],
            'sysadmin_talkloopend': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Sysadmin.SeqEvent_RemoteEvent_5',
            ],
            'toutbotpaid': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_12',
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_3',
            ],
            'trapsequencestart': [
                'Ma_Nexus_Gply.TheWorld:PersistentLevel.Main_Sequence.Chapter03._PreLeftCluster.SeqEvent_RemoteEvent_11',
            ],
            'unhidegeneratorswitch': [
                'Ma_Nexus_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'weakspotdead': [
                'Ma_Nexus_Side.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
        },
        'digsite_rk5arena_p': {
            'ambientdahlsoldiers': [
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'bunkerdied': [
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'closetopsetelevatordoors': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'destroyinjurednpc': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'elevator down': [
                'Digsite_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'elevator up': [
                'Digsite_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'intro': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'lastcall': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'maingun': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'opendoorplease': [
                'Digsite_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'opentopsetelevatordoors': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'playhallwayvo': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'rm_bossmusicoff': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'rm_bossmusicon': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'reenteroutfallvo': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'resetfightgate': [
                'Digsite_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'return1': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'return2': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'return3': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'soldiersoff': [
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'spawn_wave_four': [
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'spawn_wave_one': [
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'spawn_wave_three': [
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'spawn_wave_two': [
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'vaulthuntersighted': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'bombingrun1': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'bombingrun2': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'jink': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'retreat1': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'retreat2': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'retreat3': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'rkv': [
                'Digsite_Rk5battle.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'rkvdialogue': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'rocket': [
                'Digsite_Rk5arena_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
        },
        'outlands_p2': {
            'boomshakalaka_aideath_vo': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.Boomshakalaka.SeqEvent_RemoteEvent_5',
            ],
            'boomshakalaka_kickoffvo': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.Boomshakalaka.SeqEvent_RemoteEvent_3',
            ],
            'camerafinished': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.Boomshakalaka.SeqEvent_RemoteEvent_40',
            ],
            'dialog_teamplayerdone': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.Boomshakalaka.SeqEvent_RemoteEvent_4',
            ],
            'explosivechargesplaced': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.TreasuresOfECHOMadre.SeqEvent_RemoteEvent_3',
            ],
            'garbageshoveled01': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.TreasuresOfECHOMadre.SeqEvent_RemoteEvent_1',
            ],
            'garbageshoveled02': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.TreasuresOfECHOMadre.SeqEvent_RemoteEvent_2',
            ],
            'garbageshoveled03': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.TreasuresOfECHOMadre.SeqEvent_RemoteEvent_0',
            ],
            'homedelievry_capturedialog': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.HomeDelivery.SeqEvent_RemoteEvent_3',
            ],
            'homedelievry_rocketlaunched': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.HomeDelivery.SeqEvent_RemoteEvent_6',
            ],
            'homedelievry_turnoffdeathdialog': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.HomeDelivery.SeqEvent_RemoteEvent_1',
            ],
            'homedelivery_plantersglow': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.HomeDelivery.SeqEvent_RemoteEvent_4',
            ],
            'homedelivery_plantersglowoff': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.HomeDelivery.SeqEvent_RemoteEvent_5',
            ],
            'homedelivery_thresherfrozen': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.HomeDelivery.SeqEvent_RemoteEvent_2',
            ],
            'homedelivery_thresherthawn': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.HomeDelivery.SeqEvent_RemoteEvent_7',
            ],
            'load_skippedlistentoplan': [
                'Outlands_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'picklemovetogate': [
                'Outlands_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'plantthresher': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.HomeDelivery.SeqEvent_RemoteEvent_0',
            ],
            'spaceslam_failtimer': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.SpaceSlam.SeqEvent_RemoteEvent_3',
            ],
            'spaceslam_hideboard': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.SpaceSlam.SeqEvent_RemoteEvent_0',
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.SpaceSlam.SeqEvent_RemoteEvent_1',
            ],
            'spaceslame_firedialog': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.SpaceSlam.SeqEvent_RemoteEvent_2',
            ],
            'stopkillinglogwood': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'unlockpicklegate': [
                'Outlands_P2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'usedjetpack': [
                'Outlands_SideMissions2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
        },
        'outlands_p': {
            'audio_flowreg_explosion_1': [
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'audio_flowreg_explosion_2': [
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'audio_flowreg_pressurestart': [
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'audio_pumprelaystart': [
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'bosunpumprelaystationvo': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'bosunteasevo1': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'bridgeoverrdieused': [
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'createlavabridge': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.MethaneStation.SeqEvent_RemoteEvent_1',
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'disablereturnspawners': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'enablebridgeais': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'firstmethanedump': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.MethaneStation.SeqEvent_RemoteEvent_2',
            ],
            'flowingliquidmethane': [
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'kragon_destroyice': [
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'lavacooloff': [
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'lavahasbeencooledoff': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'methpumpaudio': [
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Outlands_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'playerenteredscavtown': [
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'pumpstationcourtyardais': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'redirectedmethaneflow2': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'resetlavaspitterspawns': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'skipperpumpstationvo': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'snipefinished': [
                'Outlands_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'spawnbadasslavaspitter': [
                'Outlands_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'turnonbridgeoverridecombat': [
                'Outlands_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
        },
        'wreck_p': {
            'aicorepickupsfx': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'ai_hub_door_switch': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'ai_hub_doors': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            'bosunambush': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'bosunambush_2': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'bosunkilledmusic': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'ch5_regulator_destroyed': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Wreck_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'ch5_stabilizer_destroyed': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'ch5_ambush_door': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'ch5_ambushers_dead': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            'chapter5_finished': [
                'Wreck_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'coresystems_exitdoor': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'drakensburg_forcefield_off': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'drakensburg_forcefield_on': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'engineroomopen': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'engineroomopenload': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'engine_fullpower': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            'engine_jettison': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'exposeflowregulator': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'exposestabilizers': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'finishedbosuntitlecard': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'flowregulatordestroyed': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'forcefieldturnedon': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.VO_CoreSystems.SeqEvent_RemoteEvent_8',
            ],
            'fullpower_combat_start': [
                'Wreck_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'muteconsolesfx': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'opensecretchamberdoor': [
                'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'playbosuntitlecard': [
                'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'poop_splat': [
                'Wreck_Int1.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'secretchamber_openelevator': [
                'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'secretchamber_spawnecho2scavs': [
                'Wreck_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'spawnwave_before_regulator': [
                'Wreck_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'spawn_littlebuddy': [
                'Wreck_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'stopengineambientshake': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'turretambush': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'turretambush_2': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'unmuteconsolesfx': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'vo_bosunhistory_complete': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            'vo_bosun_dead': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'vo_bosun_dying': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'vo_dahlsamsite': [
                'Wreck_Combat2.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'vo_drakensburgentered': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'vo_enginejettisonstart': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'vo_forcefieldturnedon': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'vo_forcefield_off': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'vo_foundengineroom': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'vo_fullpower': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            'vo_met_skipper': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'vo_regulatordestroyed': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'vo_stabilizeropening': [
                'Wreck_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'vo_stabilizers_destroyed': [
                'Wreck_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            're_hidelittlebuddymesh': [
                'Wreck_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
        },
        'deadsurface_p': {
            'are_electroniccamera': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_2',
            ],
            'are_electroniccameratwo': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_3',
            ],
            'are_electronicobject': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_1',
            ],
            'are_electronicobjectthree': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_0',
            ],
            'are_electronicobjecttwo': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_4',
            ],
            'are_lastrequestechopickedup': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Last_Requests.SeqEvent_RemoteEvent_0',
            ],
            'are_letterd': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Nel_Egg.SeqEvent_RemoteEvent_0',
            ],
            'are_letterk': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Nel_Egg.SeqEvent_RemoteEvent_1',
            ],
            'are_placedd': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Nel_Egg.SeqEvent_RemoteEvent_2',
            ],
            'are_placedk': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Nel_Egg.SeqEvent_RemoteEvent_3',
            ],
            'are_printeron': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Motivation.SeqEvent_RemoteEvent_0',
            ],
            'closedeadliftinsulatedgate': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_2',
            ],
            'eastereggstart': [
                'Deadsurface_Combat.TheWorld:PersistentLevel.Main_Sequence.FUN.SeqEvent_RemoteEvent_0',
            ],
            'fireworks': [
                'Deadsurface_Combat.TheWorld:PersistentLevel.Main_Sequence.FUN.SeqEvent_RemoteEvent_1',
            ],
            're_activatecurrentelectricplates': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_8',
            ],
            're_begindeadliftcard': [
                'Deadsurface_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_deadliftcardcomplete': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_1',
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_6',
            ],
            're_deadliftisdead': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Challenges.SeqEvent_RemoteEvent_3',
            ],
            're_disableallelectricplates': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_10',
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_19',
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_20',
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_21',
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_22',
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_41',
            ],
            're_disableoxygen': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqEvent_RemoteEvent_0',
            ],
            're_enableextrakraggons': [
                'Deadsurface_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_followjaneytohut': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqEvent_RemoteEvent_2',
            ],
            're_fusedialogcomplete': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_0',
            ],
            're_janeybonza': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_12',
            ],
            're_janeycardcomplete': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqEvent_RemoteEvent_1',
            ],
            're_janeyspawned': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_7',
            ],
            're_playvsmatinee': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_1',
            ],
            're_playerfuse_audio': [
                'Deadsurface_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_terminalsparks_audio': [
                'Deadsurface_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_turnonguysdownthepath': [
                'Deadsurface_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'rm_angrynel': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Last_Requests.SeqEvent_RemoteEvent_5',
            ],
            'rm_nel': [
                'Deadsurface_Combat.TheWorld:PersistentLevel.Main_Sequence.Nel.SeqEvent_RemoteEvent_1',
            ],
            'rm_neldead': [
                'Deadsurface_Combat.TheWorld:PersistentLevel.Main_Sequence.Nel.SeqEvent_RemoteEvent_2',
            ],
            'rm_nelkilltime': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Last_Requests.SeqEvent_RemoteEvent_2',
            ],
            'rm_novashield': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_5',
            ],
            'reopendeadliftinsulatedgate': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_4',
            ],
            'stopdeadliftaddwavetimer': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_9',
            ],
            'turnonfloorplategroup1': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_3',
            ],
            'turnonfloorplategroup2': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_11',
            ],
            'turnonfloorplategroup3': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_16',
            ],
            'turnonfloorplategroup4': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_17',
            ],
            'turnonfloorplategroup5': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_14',
            ],
            'turnonfloorplategroup6': [
                'Deadsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_5',
            ],
        },
        'randdfacility_p': {
            'active_rd_open': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'boom': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_33',
            ],
            'bringintarget': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_PickingUpThePieces.SeqEvent_RemoteEvent_2',
            ],
            'camerachallengetest': [
                'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SS_Cameras.SeqEvent_RemoteEvent_1',
            ],
            'coolleavingdialogdone': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            'dontlookat': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_38',
            ],
            'drlspawned': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'enablefinaltypedan': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_40',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_7',
            ],
            'enablefinaltypehal': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_41',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_8',
            ],
            'exit': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'exituncloaked': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_320.SeqEvent_RemoteEvent_9',
            ],
            'explode': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'fire_laser': [
                'RandDFacility_FX.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'grabbeardialogdone': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'keep_rd_open': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
            ],
            'lookatpeople': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_37',
            ],
            'on_turn_in': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'pointtest': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_activatebearreturn': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_attachtoevent': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_7',
            ],
            're_beargrabdialogdone': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            're_brainspawned': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_15',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_32',
            ],
            're_challengecameradestroyed': [
                'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SS_Cameras.SeqEvent_RemoteEvent_0',
            ],
            're_changeauth': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_5',
            ],
            're_coolimleaving': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_540.SeqEvent_RemoteEvent_52',
            ],
            're_decompression_audio': [
                'RandDFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_disabletyping': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_30',
            ],
            're_drainaquarium': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_drainblooda': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_37',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_4',
            ],
            're_drainbloodb': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_38',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_5',
            ],
            're_drainbloodc': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_3',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_36',
            ],
            're_enablesacrifice': [
                'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_enabletakephoto': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_enabletyping': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_29',
            ],
            're_findphotodialogdone': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_170.SeqEvent_RemoteEvent_0',
            ],
            're_firethatlaser': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_PickingUpThePieces.SeqEvent_RemoteEvent_0',
            ],
            're_firetheanimalrocket': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_13',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_2',
            ],
            're_firethecomborocket': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_1',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_22',
            ],
            're_firetheskavrocket': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_0',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_17',
            ],
            're_freakinsick': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_12',
            ],
            're_gspawn': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_39',
            ],
            're_getminteoffperch': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_FreshAir.SeqEvent_RemoteEvent_2',
            ],
            're_grabbear': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_441.SeqEvent_RemoteEvent_19',
            ],
            're_grasonloccheck': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            're_graysonpressbutton': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            're_humanbraindropped': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_30',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_31',
            ],
            're_jacktassconvo': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_040.SeqEvent_RemoteEvent_9',
            ],
            're_keycardstalkerdied': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_300.SeqEvent_RemoteEvent_4',
            ],
            're_killbeasts': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_130.SeqEvent_RemoteEvent_11',
            ],
            're_killdan': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_3',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_31',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_36',
            ],
            're_killhall': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_2',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_32',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_35',
            ],
            're_killmoretorks': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_420.SeqEvent_RemoteEvent_14',
            ],
            're_knock': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            're_lab19_lowerdoor': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_0',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_10',
            ],
            're_labdooropenload': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_3',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_9',
            ],
            're_letdialoghappen': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            're_movearmup': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_27',
            ],
            're_moveminte': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_FreshAir.SeqEvent_RemoteEvent_16',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_160.SeqEvent_RemoteEvent_16',
            ],
            're_moveminteback': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_FreshAir.SeqEvent_RemoteEvent_18',
            ],
            're_movetochest1': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_nakayamadialogdone': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_2',
            ],
            're_openaqdoor': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            're_openaqaccessdoor': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_openbraindoor': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            're_opencage': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_8',
            ],
            're_opennumberplate': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_1',
            ],
            're_openobservationdoor': [
                'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_openobservationdoornoscan': [
                'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_openscionedoor': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_opentorresdoor': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_plateopened': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_4',
            ],
            're_playergrabbedbear': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_450.SeqEvent_RemoteEvent_22',
            ],
            're_pointtobear': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_440.SeqEvent_RemoteEvent_16',
            ],
            're_pressthebuttondialog': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_24',
            ],
            're_readytofreeze': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_21',
            ],
            're_returntopath': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_27',
            ],
            're_reversearm': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_1',
            ],
            're_sci1dialogdone': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_190.SeqEvent_RemoteEvent_18',
            ],
            're_sci1introline': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_080.SeqEvent_RemoteEvent_10',
            ],
            're_sci3cometowindow': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            're_sci3lostkeys': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_210.SeqEvent_RemoteEvent_2',
            ],
            're_scitwoscream': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_410.SeqEvent_RemoteEvent_12',
            ],
            're_setsecondbutton': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_16',
            ],
            're_setupmintedialog': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_131.SeqEvent_RemoteEvent_17',
            ],
            're_skavrocketimpact': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_18',
            ],
            're_sorrydialogdone': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_002.SeqEvent_RemoteEvent_0',
            ],
            're_sparadontlookat': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_35',
            ],
            're_sparalookat': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_34',
            ],
            're_spawnbadasstork': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_441.SeqEvent_RemoteEvent_20',
            ],
            're_stalkerspawned': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_291.SeqEvent_RemoteEvent_3',
            ],
            're_stalkerwingpickedup': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_29',
            ],
            're_stalkerscomment': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_430.SeqEvent_RemoteEvent_12',
            ],
            're_stalkerskilled': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_startblender': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_11',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_25',
            ],
            're_startdialog': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_5',
            ],
            're_startreturndialog': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_6',
            ],
            're_startsci1move': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_190.SeqEvent_RemoteEvent_7',
            ],
            're_suckanimalbrain': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_20',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_7',
            ],
            're_talkfreshairscientist': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_FreshAir.SeqEvent_RemoteEvent_5',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_FreshAir.SeqEvent_RemoteEvent_6',
            ],
            're_torkaggro': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_000.SeqEvent_RemoteEvent_0',
            ],
            're_torkbraindropped': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_28',
            ],
            're_torksucks': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_26',
            ],
            're_torrestesting': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            're_uncloakdoor': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_uncloakexit': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_320.SeqEvent_RemoteEvent_5',
            ],
            're_unlockcoraltube': [
                'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_windowclose': [
                'RandDFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_FreshAir.SeqEvent_RemoteEvent_0',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_FreshAir.SeqEvent_RemoteEvent_4',
            ],
            're_windowopen': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_FreshAir.SeqEvent_RemoteEvent_1',
            ],
            're_windowopen_audio': [
                'RandDFacility_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_wrongnum': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_6',
            ],
            're_yeahyeah': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_14',
            ],
            're_bearpointfinished': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_openscientist2door': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            're_rewindtorresdoor': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            're_setcomborocket': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_9',
            ],
            'rs_3rdrocketimpact': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_23',
            ],
            're_startcheer': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'setupboltchoose': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_4',
            ],
            'spawnx': [
                'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'testcombat': [
                'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'test_labstart': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Lab19.SeqEvent_RemoteEvent_11',
            ],
            'lloyd': [
                'RandDFacility_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'movearm': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_Loop.SeqEvent_RemoteEvent_0',
            ],
            'raisestand': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_PickingUpThePieces.SeqEvent_RemoteEvent_34',
            ],
            're_jackgladstonedialog': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_370.SeqEvent_RemoteEvent_10',
            ],
            're_suckhumanbrain': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_10',
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_19',
            ],
            're_enablestalkerline': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_getattnetion': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_000.SeqEvent_RemoteEvent_7',
            ],
            're_gladstonebacktooffice': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_VO.SS_002.SeqEvent_RemoteEvent_8',
            ],
            're_scream': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_FreshAir.SeqEvent_RemoteEvent_3',
            ],
            're_setanimalrocket': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_6',
            ],
            're_setskavrocket': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_RocketSurgery.SeqEvent_RemoteEvent_8',
            ],
            'testchest': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SS_PickingUpThePieces.SeqEvent_RemoteEvent_1',
            ],
            'testextend': [
                'RandDFacility_Mission.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
        },
        'moonsurface_p': {
            'are_electroniccamera': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_2',
            ],
            'are_electroniccameratwo': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_3',
            ],
            'are_electronicobject': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_1',
            ],
            'are_electronicobjectthree': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_0',
            ],
            'are_electronicobjecttwo': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_4',
            ],
            'are_lastrequestechopickedup': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Last_Requests.SeqEvent_RemoteEvent_0',
            ],
            'are_letterd': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Nel_Egg.SeqEvent_RemoteEvent_0',
            ],
            'are_letterk': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Nel_Egg.SeqEvent_RemoteEvent_1',
            ],
            'are_placedd': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Nel_Egg.SeqEvent_RemoteEvent_2',
            ],
            'are_placedk': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Nel_Egg.SeqEvent_RemoteEvent_3',
            ],
            'are_printeron': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Motivation.SeqEvent_RemoteEvent_0',
            ],
            'beaconrocketlanded': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Zapped_3.SeqEvent_RemoteEvent_1',
            ],
            'kraggonmad': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ToroToro.SeqEvent_RemoteEvent_1',
            ],
            're_disableoxygen': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqEvent_RemoteEvent_0',
            ],
            're_enableextrakraggons': [
                'Moonsurface_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_followjaneytohut': [
                'Moonsurface_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqEvent_RemoteEvent_2',
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter01.SeqEvent_RemoteEvent_3',
            ],
            're_fusedialogcomplete': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_0',
            ],
            're_janeygreetsyoufromoutside': [
                'Moonsurface_Cinematic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_janeyspawned': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter02.SeqEvent_RemoteEvent_7',
            ],
            're_playerfuse_audio': [
                'Moonsurface_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_terminalsparks_audio': [
                'Moonsurface_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'rm_angrynel': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Last_Requests.SeqEvent_RemoteEvent_5',
            ],
            'rm_nelkilltime': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Last_Requests.SeqEvent_RemoteEvent_2',
            ],
            'rm_novashield': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.NovaNoProblem.SeqEvent_RemoteEvent_5',
            ],
            'rm_resetskeet': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.skeet_shooting.SeqEvent_RemoteEvent_1',
            ],
            'rm_resetskeet2': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.skeet_shooting.SeqEvent_RemoteEvent_2',
            ],
            'rm_resetskeet3': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.skeet_shooting.SeqEvent_RemoteEvent_0',
            ],
            'spawnskeet': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.skeet_shooting.SeqEvent_RemoteEvent_6',
            ],
            'startbeaconmat': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Zapped_3.SeqEvent_RemoteEvent_4',
            ],
            'zapped3_shipimpact': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Zapped_3.SeqEvent_RemoteEvent_2',
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Zapped_3.SeqEvent_RemoteEvent_3',
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Zapped_3.SeqEvent_RemoteEvent_7',
            ],
            'zapped_startshipmat': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Zapped_3.SeqEvent_RemoteEvent_5',
            ],
            'chosetorgue': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ToroToro.SeqEvent_RemoteEvent_2',
            ],
            'springturnin': [
                'Moonsurface_Dynamic.TheWorld:PersistentLevel.Main_Sequence.ToroToro.SeqEvent_RemoteEvent_0',
            ],
        },
        'stantonsliver_p': {
            'excalibastardtaken': [
                'StantonsLiver_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'littlecreatureskilledscav': [
                'StantonsLiver_SideMissions.TheWorld:PersistentLevel.Main_Sequence.AllTheLittleCreatures.SeqEvent_RemoteEvent_0',
            ],
            'makewheelsusable': [
                'StantonsLiver_SideMissions.TheWorld:PersistentLevel.Main_Sequence.AllTheLittleCreatures.SeqEvent_RemoteEvent_4',
            ],
            'playeraskednicely': [
                'StantonsLiver_SideMissions.TheWorld:PersistentLevel.Main_Sequence.Grinders.SeqEvent_RemoteEvent_29',
            ],
            'rumblingsequence': [
                'StantonsLiver_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'StantonsLiver_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'StantonsLiver_SideMissions.TheWorld:PersistentLevel.Main_Sequence.AllTheLittleCreatures.SeqEvent_RemoteEvent_5',
            ],
            'startrocketsfx': [
                'StantonsLiver_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'stoprocketsfx': [
                'StantonsLiver_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'torkfrozen': [
                'StantonsLiver_SideMissions.TheWorld:PersistentLevel.Main_Sequence.Zapped.SeqEvent_RemoteEvent_0',
            ],
            'torkunfrozen': [
                'StantonsLiver_SideMissions.TheWorld:PersistentLevel.Main_Sequence.Zapped.SeqEvent_RemoteEvent_2',
            ],
        },
        'sublevel13_p': {
            'destroyedconsole1': [
                'Sublevel13_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'destroyedconsole2': [
                'Sublevel13_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'destroyedconsole3': [
                'Sublevel13_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'doorlocked': [
                'Sublevel13_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'junctionboxused': [
                'Sublevel13_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'queenspawn': [
                'Sublevel13_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'sublevel13_unlockelevator': [
                'Sublevel13_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'ventused': [
                'Sublevel13_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
        },
        'ma_subconscious_p': {
            'aireadytodig': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_6',
            ],
            'answeredsponxriddle': [
                'Ma_Subconscious_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'beamshse': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_1',
            ],
            'binkdone': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_0',
            ],
            'bobblejack': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_16',
            ],
            'bubblespopped': [
                'Ma_Subconscious_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'closetransition': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Sub-Subconscious.SeqEvent_RemoteEvent_1',
            ],
            'freehope': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_10',
            ],
            'freeselfesteem': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_19',
            ],
            'ifeelfunny': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_14',
            ],
            'jackopen': [
                'Ma_Subconscious_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'memoryover': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_4',
            ],
            'nearbadtrap': [
                'Ma_Subconscious_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'opensubboss': [
                'Ma_Subconscious_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'opentransition': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Sub-Subconscious.SeqEvent_RemoteEvent_0',
            ],
            'outsideshard': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_11',
            ],
            'playhsematinee': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_12',
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_3',
            ],
            'returnhopeselfesteem': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_5',
            ],
            'shardgate': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_13',
            ],
            'showjumppadislands': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_17',
            ],
            'showmatineehse': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_18',
            ],
            'startdigging': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_9',
            ],
            'startdiggingnow': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_20',
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_7',
            ],
            'startoriginstory': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_2',
            ],
            'stopdigging': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_8',
            ],
            'swapdoor': [
                'Ma_Subconscious_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'talkmetatraphse': [
                'Ma_Subconscious_Game.TheWorld:PersistentLevel.Main_Sequence.Chapter5___Subconscious.SeqEvent_RemoteEvent_15',
            ],
            'talkedtotkbaha': [
                'Ma_Subconscious_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
        },
        'dahlfactory_p': {
            'aicoreinstalled_stingrayfrontdoor': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeStingRay.SeqEvent_RemoteEvent_1',
            ],
            'audio_atriumdoor': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'audio_conveyorconsoleused': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'audio_fuseboxoff': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'audio_gladstone_door_01': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'audio_gladstone_door_02': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'audio_gladstone_door_03': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'audio_holostart_01': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'audio_holostart_02': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'audio_holostop_01': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'audio_holostop_02': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'audio_stationconsole_used': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'audio_steamstart': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'audio_stingraydoor': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'audio_trapoff': [
                'DahlFactory_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'badasstorkdialog': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_0',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_3',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_6',
            ],
            'conveyorbelt_movecontainer': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Train_Station.SeqEvent_RemoteEvent_0',
            ],
            'dahlfactory_turnononewayswitch': [
                'DahlFactory_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'dahlpowerloader_closedoors': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_0',
            ],
            'dahlpowersuit_abortmove': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_31',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_32',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_33',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_34',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_35',
            ],
            'dahlpowersuit_doorsclosed': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_27',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_28',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_43',
            ],
            'dahlpowersuit_opendoors': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_29',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_29',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_30',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_36',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_41',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_42',
            ],
            'dialog_beforestingrayturretswitch': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_9',
            ],
            'dialog_conveyorconsoleused': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_10',
            ],
            'dialog_findnavconsole1': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_5',
            ],
            'dialog_gladstoneareaturrets': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_15',
            ],
            'dialog_gladstoneattention': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_12',
            ],
            'dialog_killthat': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_4',
            ],
            'dialog_meetgladstone': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_16',
            ],
            'dialog_startinglinesdone': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_17',
            ],
            'dialog_torkline1': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_18',
            ],
            'dialog_torktrashcanspawn': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_11',
            ],
            'dialog_trainstationconsoleused': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_1',
            ],
            'firestationbeam': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'gladstoneopensdoor': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_GladstoneArea.SeqEvent_RemoteEvent_14',
            ],
            'gladstone_closewindows': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_GladstoneArea.SeqEvent_RemoteEvent_0',
            ],
            'gladstone_loaderhologramstart': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_GladstoneArea.SeqEvent_RemoteEvent_13',
            ],
            'gladstone_totable': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_GladstoneArea.SeqEvent_RemoteEvent_3',
            ],
            'io_pipecontrols_turnpipe': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeStingRay.SeqEvent_RemoteEvent_6',
            ],
            'openconveyordoor': [
                'DahlFactory_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Train_Station.SeqEvent_RemoteEvent_1',
                'DahlFactory_TStation.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'opengladstoneareastartingdoor': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_GladstoneArea.SeqEvent_RemoteEvent_15',
            ],
            'opengladstoneexitdoor': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_2',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_GladstoneArea.SeqEvent_RemoteEvent_2',
            ],
            'playerdamagedturret_beforestingray': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_7',
            ],
            'powersuitdoor_banditshurt': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_23',
            ],
            'powersuitdoor_banditsretreat': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_24',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_24',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_25',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_37',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_38',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_39',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_40',
            ],
            'powersuitskilled': [
                'DahlFactory_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'scavs ready to fight': [
                'DahlFactory_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'spawngarageopener': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Train_Station.SeqEvent_RemoteEvent_2',
            ],
            'stationbeamfired': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'stingrayatrium_torkattack': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_Atrium.SeqEvent_RemoteEvent_0',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_Atrium.SeqEvent_RemoteEvent_1',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_Atrium.SeqEvent_RemoteEvent_18',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_Atrium.SeqEvent_RemoteEvent_2',
            ],
            'stingrayatrium_torkattackspawn': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.StingRay_Atrium.SeqEvent_RemoteEvent_3',
            ],
            'stingrayroom2_combatresolved': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_14',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_3',
            ],
            'stingrayfactroydoorsclosed': [
                'DahlFactory_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'stringrayfrontdoorclosed': [
                'DahlFactory_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'DahlFactory_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_13',
            ],
            'stringrayfrontdoor_combatresolved': [
                'DahlFactory_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Dialog.SeqEvent_RemoteEvent_8',
            ],
            'playerarrivedrobotfacilityfrontdoor': [
                'DahlFactory_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Outside_BeforeRobotics.SeqEvent_RemoteEvent_22',
            ],
        },
        'dahlfactory_boss': {
            'aicoreinstallmatcomplete': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_2',
            ],
            'aicoreinstalled_powersuit': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.InstallAICore.SeqEvent_RemoteEvent_4',
            ],
            'aicorespawned': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.InstallAICore.SeqEvent_RemoteEvent_7',
            ],
            'aicoretolegsplacement': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqEvent_RemoteEvent_4',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqEvent_RemoteEvent_5',
            ],
            'aicore_movetonode1': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqEvent_RemoteEvent_11',
            ],
            'aicore_reacionanimdone': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqEvent_RemoteEvent_3',
            ],
            'aicore_readyfordetonation': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_25',
            ],
            'abortfordeath': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'attachturretsmat': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqEvent_RemoteEvent_3',
            ],
            'audio_dahlbossdoor_start_01': [
                'DahlFactory_Boss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'audio_dahlbossdoor_start_02': [
                'DahlFactory_Boss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'audio_dahlbossdoor_start_03': [
                'DahlFactory_Boss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'audio_dahlboss_poweron': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_12',
                'DahlFactory_Boss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'audio_dahl_security': [
                'DahlFactory_Boss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'barricadedestroyed': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'bossaicoreinstalled': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_1',
            ],
            'bosslegsdead': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_1',
            ],
            'bossturretdied': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'cleanupenemiesbeforeskipper': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_23',
            ],
            'closetreasuredoorforrunnableboss': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_3',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_6',
            ],
            'corebossdefeated': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_27',
            ],
            'corebossdefeated_runnable': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'dahlfactory_turnononewayswitch': [
                'DahlFactory_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'destroyloaders1': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            'dialog_aicoreerase': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.RobotBoss_TitleCard.SeqEvent_RemoteEvent_42',
            ],
            'dialog_aicorefeeldirty': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_37',
            ],
            'dialog_aicorekilledbadguy': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_36',
            ],
            'dialog_aicorenewbody': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_16',
            ],
            'dialog_aiseepowersuits': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_4',
            ],
            'dialog_attachlegs': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_8',
            ],
            'dialog_bossdisabled': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_0',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_13',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_4',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_5',
                'DahlFactory_Boss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'dialog_getawesome': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_2',
            ],
            'dialog_gladstonesorry': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_45',
            ],
            'dialog_hardworkfinished': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_22',
            ],
            'dialog_headtolegs': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_24',
            ],
            'dialog_headtoturretarea': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_19',
            ],
            'dialog_legsattached': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_21',
            ],
            'dialog_loadersattacking': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_39',
            ],
            'dialog_lookathergo': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_5',
            ],
            'dialog_opentorsocage': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_33',
            ],
            'dialog_pickituplinefinished': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_34',
            ],
            'dialog_pissoff': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_9',
            ],
            'dialog_playerkilledscav_turretarea': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_23',
            ],
            'dialog_plugmein': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_35',
            ],
            'dialog_securitybots': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_31',
            ],
            'dialog_shrinkage': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_10',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_10',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_13',
            ],
            'dialog_skippererase': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_47',
            ],
            'dialog_startwipe': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_3',
            ],
            'dialog_turnrail': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_28',
            ],
            'dialog_windowcover': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_11',
            ],
            'disabledlegsdialogdone': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_30',
            ],
            'eyecreation_spawneye': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Eye_Creation_Area.SeqEvent_RemoteEvent_0',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_0',
            ],
            'freezewindow_releasescavai': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_0',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_1',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_11',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_12',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_14',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_9',
            ],
            'gotonewspot': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'hideskipperbossbar': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'iamcore': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'jackskippercopydialogdone': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_14',
            ],
            'legsattached': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Prototype_Moving.SeqEvent_RemoteEvent_0',
            ],
            'mounttorsocrane': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Prototype_Moving.SeqEvent_RemoteEvent_2',
            ],
            'movethebotbody': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'openaiescortgate': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'opendoorstoturretlegsarea': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqEvent_RemoteEvent_2',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqEvent_RemoteEvent_3',
            ],
            'openfinalroomdoor': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Prototype_Moving.SeqEvent_RemoteEvent_7',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_FinalArea.SeqEvent_RemoteEvent_7',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_7',
            ],
            'opensecuritybotspawninggate': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'opensecurtiybotdoors': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TorsoArea.SeqEvent_RemoteEvent_1',
            ],
            'openturretareadoor1': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqEvent_RemoteEvent_12',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqEvent_RemoteEvent_14',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqEvent_RemoteEvent_20',
            ],
            'openturretgate': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'openwindowcover': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_8',
            ],
            'powerroomcombatresolved': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_29',
            ],
            'rb_tc_elevatordialogwait': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.RobotBoss_TitleCard.SeqEvent_RemoteEvent_44',
            ],
            'rb_tc_elevatorfinished': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.RobotBoss_TitleCard.SeqEvent_RemoteEvent_2',
            ],
            're_disablebossspawnvolumetesting': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            'railsystemturned': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Prototype_Moving.SeqEvent_RemoteEvent_1',
            ],
            'reversetorsobumpmat': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqEvent_RemoteEvent_0',
            ],
            'roboboss_turnoffreset': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'runnableroboboss': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.RobotBoss_TitleCard.SeqEvent_RemoteEvent_4',
            ],
            'savestateroboboss': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.RobotBoss_TitleCard.SeqEvent_RemoteEvent_3',
            ],
            'scanforbarricadetarget': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'scavwalla_cheer_start': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_5',
            ],
            'scavwalla_cheer_stop': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_4',
            ],
            'scavwalla_disappoint_start': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_7',
            ],
            'scavwalla_disappoint_stop': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_6',
            ],
            'scavwalla_start': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_2',
            ],
            'scavwalla_stop': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Power_Room.SeqEvent_RemoteEvent_3',
            ],
            'skipperend_cleardialog': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_40',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_41',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_42',
            ],
            'spawnboss': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'spawnloaders1': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'spawnloaders1done': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_26',
            ],
            'spawnloaders2': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'spawnloaders2done': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_38',
            ],
            'spawnrunnableboss': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'start_railsystemmat': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_FinalArea.SeqEvent_RemoteEvent_0',
            ],
            'testspawnwithtc': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.RobotBoss_TitleCard.SeqEvent_RemoteEvent_1',
            ],
            'titlecardend': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_15',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_15',
                'DahlFactory_Boss_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'toasterlinecomplete': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_32',
            ],
            'torsaarea_combatresolved1': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Boss_Area.SeqEvent_RemoteEvent_18',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_18',
            ],
            'torsomovedoutofway': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.SeqEvent_RemoteEvent_1',
            ],
            'torsoroom_startcombat': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'turnonaicorekilllines': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_20',
            ],
            'turnondronewallprotection': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'turnoffaicorekilllines': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_17',
            ],
            'turnonloadstate_aicoregetup': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_LegsArea.InstallAICore.SeqEvent_RemoteEvent_0',
            ],
            'turnonrobotturrets_finalroom': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Prototype_SaveState.SeqEvent_RemoteEvent_6',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.mission_flow_events.SeqEvent_RemoteEvent_6',
            ],
            'turnonsecurtiybotscavs': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'turretcalibration_turret1online': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqEvent_RemoteEvent_0',
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqEvent_RemoteEvent_2',
            ],
            'turretcalibration_turret2online': [
                'DahlFactory_BossDynamic.TheWorld:PersistentLevel.Main_Sequence.Robotics_TurretCalibrationArea.SeqEvent_RemoteEvent_8',
            ],
            'unlockpoint_zonea': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'unlockpoint_zoneb': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'unlockpoint_zonec': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'warehouse_dooropened': [
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.FinalRoomCombat.SeqEvent_RemoteEvent_22',
                'DahlFactory_BossCombat.TheWorld:PersistentLevel.Main_Sequence.FinalRoomCombat.SeqEvent_RemoteEvent_6',
            ],
        },
        'moon_p': {
            'audio_scrambler': [
                'Moon_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'ch4_pauseskymatinee': [
                'Moon_SkyDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'ch4_startskymatinee': [
                'Moon_SkyDynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'concordiagateopen': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'enablecaveshugguraths': [
                'Moon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'enableintercom': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqEvent_RemoteEvent_4',
            ],
            'enableposterbarrels': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.RecruitmentDrive.SeqEvent_RemoteEvent_0',
            ],
            'endsalute': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.VoyageOfCaptainChef.SeqEvent_RemoteEvent_15',
            ],
            'firestationbeam': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'firstornamentdropped': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqEvent_RemoteEvent_6',
            ],
            'fishtailing_spawnstingray': [
                'Moon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'fishtailing_startlineflares': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_19',
            ],
            'fishtailing_timer': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_27',
            ],
            'fishtailing_timesup': [
                'Moon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'fishtailing_waypointflares01': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_9',
            ],
            'fishtailing_waypointflares02': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_20',
            ],
            'fishtailing_waypointflares03': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_22',
            ],
            'fishtailing_waypointflares04': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_21',
            ],
            'fishtailing_waypointflares05': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_17',
            ],
            'fishtailing_waypointflares06': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_18',
            ],
            'fishtailing_waypointflares07': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_23',
            ],
            'fishtailing_waypointflares08': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_24',
            ],
            'fishtailing_waypointflares09': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_36',
            ],
            'fishtailing_waypointflares10': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_16',
            ],
            'fishtailing_waypointflares11': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_2',
            ],
            'fishtailing_waypointflares12': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_1',
            ],
            'fishtailing_waypointflares13': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_0',
            ],
            'fishtailing_waypointflares15': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.PopRacing.SeqEvent_RemoteEvent_26',
            ],
            'flaghoisted01': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.VoyageOfCaptainChef.SeqEvent_RemoteEvent_6',
            ],
            'flaghoisted02': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.VoyageOfCaptainChef.SeqEvent_RemoteEvent_8',
            ],
            'flaghoisted03': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.VoyageOfCaptainChef.SeqEvent_RemoteEvent_28',
            ],
            'gotastingray': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_5_AI_Core.SeqEvent_RemoteEvent_0',
                'Moon_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'grinders_killscavbuggy': [
                'Moon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'grinders_scavbuggykilled': [
                'Moon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'hannadead': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.Zone_4.SeqEvent_RemoteEvent_2',
            ],
            'killedhalf': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqEvent_RemoteEvent_3',
            ],
            'lastbadassspawned': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqEvent_RemoteEvent_0',
            ],
            'nearcaptainchef': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.VoyageOfCaptainChef.SeqEvent_RemoteEvent_1',
            ],
            'opencrisisscartomoongate': [
                'Moon_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'pickupreminder': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqEvent_RemoteEvent_2',
            ],
            'playguitar': [
                'Moon_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'playtobiasecho': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_checkagain': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_5_AI_Core.SeqEvent_RemoteEvent_2',
            ],
            're_combopassed': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_5_AI_Core.SeqEvent_RemoteEvent_1',
            ],
            'reporttoscavtrp': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqEvent_RemoteEvent_1',
            ],
            'scavtrpdebrief': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqEvent_RemoteEvent_7',
            ],
            'scavtrpgateopen': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'scavtrproutine': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'scavquestioned': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.AnotherPickle.SeqEvent_RemoteEvent_0',
            ],
            'scavtrp2lines': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'scavtrp4lines': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'scavsaggressive': [
                'Moon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
                'Moon_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'scavsneutral': [
                'Moon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'secretentranceopen': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'shackslammed': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'shuggurathsspawned': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.BunchOfIceHoles.SeqEvent_RemoteEvent_0',
            ],
            'shugurathskilled': [
                'Moon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'skylightbarrelsexploded': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.RecruitmentDrive.SeqEvent_RemoteEvent_1',
            ],
            'startrocketsfx': [
                'Moon_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'startvehiclespawnglow': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'stationbeamfired': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.Chapter_4_New_Direction.SeqEvent_RemoteEvent_5',
            ],
            'stoprocketsfx': [
                'Moon_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'stopvehcilespawnglow': [
                'Moon_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'toarms_timpotpicked': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.ToArms.SeqEvent_RemoteEvent_0',
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.ToArms.SeqEvent_RemoteEvent_6',
            ],
            'toarms_tompotpicked': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.ToArms.SeqEvent_RemoteEvent_2',
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.ToArms.SeqEvent_RemoteEvent_5',
            ],
            'toarms_tumpotpicked': [
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.ToArms.SeqEvent_RemoteEvent_1',
                'Moon_SideMissions.TheWorld:PersistentLevel.Main_Sequence.ToArms.SeqEvent_RemoteEvent_4',
            ],
            'trainarrived': [
                'Moon_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'traincalled': [
                'Moon_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            're_tothemoon_showblood': [
                'Moon_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
        },
        'access_p': {
            'accessvo00': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'accessvo01': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'accessvo02': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'accessvo03': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'accessvo04': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'accessvo05': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'accessvo06': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'accessvo07': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            'accessvo08': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'cannonbest': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'dialog587': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'dialog588': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'finalrun': [
                '11B_Facility_A_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'fireon': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'gogogo': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'gotthrough': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'shieldlastframe': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'shieldplay': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'shieldreverse': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'shieldshot': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'spawnputti': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'z8ntrp_enddraw': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            'z8ntrp_gaveputti': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'z8ntrp_handovervol': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'z8ntrp_postflav': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'z8ntrp_random': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'z8ntrp_rescued': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'z8ntrp_start': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'z8ntrp_turnin': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'z8ntrp_opendraw': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'closevo': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'didntmakeit': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'liftinplace': [
                '11B_Access_GAME.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Access_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            'secretopen': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'shieldvo': [
                'Access_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
        },
        'innerhull_p': {
            'clap_l3k_damagedbyother': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_8',
            ],
            'clap_l3k_damagedbyplayer': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_11',
            ],
            're_activatefailsafe': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.BackOnSchedule.SeqEvent_RemoteEvent_0',
            ],
            're_activateforcefield_1': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_41',
            ],
            're_activateforcefield_2': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_42',
            ],
            're_activateforcefield_3': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_43',
            ],
            're_activateforcefield_4': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_44',
            ],
            're_activateforcefield_5': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            're_activatequarantinekillden': [
                'InnerHull_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_airlock_01_blow': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_airlock_01_suck': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_airlock_02_blow': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_airlock_02_suck': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_airlock_03_blow': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_airlock_03_suck': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_airlock_04_blow': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            're_airlock_04_suck': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_alarmfast': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            're_alarmstop': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
            ],
            're_blowtheexit_complete': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_8',
            ],
            're_blow_the_exit': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            're_blow_the_hall': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_46',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_47',
            ],
            're_bonusdebrishit': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_14',
            ],
            're_bonusmeteorshit': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_20',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_27',
            ],
            're_bonuspatrolshit': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_28',
            ],
            're_bot_final_pipe': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            're_clap_l3k_attackvo': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_5',
            ],
            're_clap_l3k_spawned': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_9',
            ],
            're_clap_l3k_voclear': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_20',
            ],
            're_clap_l3k_voclose': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_12',
            ],
            're_closeaccessportals': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_33',
            ],
            're_closecockyvogate': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_26',
            ],
            're_closejackminordialogs': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_13',
            ],
            're_closemidmaintdoors': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            're_closenonicedamagevo': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_2',
            ],
            're_closeoxygendoors': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_45',
            ],
            're_closetakedamagevogate': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_2',
            ],
            're_eghoodbotkill': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_7',
            ],
            're_eghoodplayerkill': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_10',
            ],
            're_eghoodspawnadds': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_2',
            ],
            're_eghood_playerdamage': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_0',
            ],
            're_fabeffect_off': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_4',
            ],
            're_fabeffect_on': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_14',
            ],
            're_finalfreezegate': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_0',
            ],
            're_firstboil_vo': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_5',
            ],
            're_firstlaserfirevo': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_10',
            ],
            're_firstratdahlbattle_vo': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_11',
            ],
            're_hallmarinesprovoked': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_7',
            ],
            're_hall_destroyed': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_50',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_51',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_52',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_54',
            ],
            're_hallwaydestruction_complete': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_3',
            ],
            're_hallwaytrigger': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_6',
            ],
            're_hideoxygenmeter': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            're_hurpdestroyed': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_3',
            ],
            're_hurpregenerated': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_1',
            ],
            're_innerhull_safedistance': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_4',
            ],
            're_killlazlo_spawn': [
                'InnerHull_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            're_lazloopendoorone': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_4',
            ],
            're_lazloopendoortwo': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.TroubleWithSpaceHurps.SeqEvent_RemoteEvent_4',
            ],
            're_lazloopenreturnone': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_5',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_7',
            ],
            're_lazlo_death': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.TroubleWithSpaceHurps.SeqEvent_RemoteEvent_1',
            ],
            're_lazlo_firstcombatroom': [
                'InnerHull_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_lazlo_firstmove': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.TroubleWithSpaceHurps.SeqEvent_RemoteEvent_2',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.TroubleWithSpaceHurps.SeqEvent_RemoteEvent_3',
            ],
            're_lazlo_secondmove': [
                'InnerHull_Combat.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.TroubleWithSpaceHurps.SeqEvent_RemoteEvent_0',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.TroubleWithSpaceHurps.SeqEvent_RemoteEvent_5',
            ],
            're_lift_1_reset': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_lift_2_reset': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            're_lift_3_reset': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            're_lift_4_reset': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
            ],
            're_lift_5_reset': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            're_lift_6_reset': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            're_lift_looping': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            're_lilith_gladiator_arirlock_vo': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_2',
            ],
            're_mid_map_laser_fire': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
            ],
            're_open_inperfecthibernatioon_gatedoors': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_17',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_25',
            ],
            're_openaccessportals': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            're_openaccessports': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.BackOnSchedule.SeqEvent_RemoteEvent_1',
            ],
            're_opencockyvogate': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_25',
            ],
            're_opendialoggate': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_6',
            ],
            're_openjackminordialogs': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_12',
            ],
            're_openmidmaintdoors': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            're_opennonicedamagevo': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_3',
            ],
            're_openoxygendoors': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_49',
            ],
            're_opentakedamagevogate': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_3',
            ],
            're_oxygen_off': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            're_oxygen_on': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            're_pipemovescomplete': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InnerHull_Plot.SeqEvent_RemoteEvent_9',
            ],
            're_platform_cycle': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            're_quarantineairlockopen': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Quarantine.SeqEvent_RemoteEvent_1',
            ],
            're_quarantine_boilspawndialog': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Quarantine.SeqEvent_RemoteEvent_2',
            ],
            're_releasedworkerbots': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            're_removelockdown': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            're_removeobstruction': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
            ],
            're_resetbuttonstate': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.BackOnSchedule.SeqEvent_RemoteEvent_21',
            ],
            're_resetfailsafetimer': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
            're_resetforcefields': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            're_resetsystem': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.BackOnSchedule.SeqEvent_RemoteEvent_4',
            ],
            're_reset_airlock': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
            ],
            're_reset_airlock_02': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            're_reset_airlock_04': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            're_reset_airlock_05': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            're_runnablebotarrived': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_23',
            ],
            're_runnabledebris1_cleared': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_16',
            ],
            're_runnabledebrishit': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_21',
            ],
            're_runnablemeteorshit': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_22',
            ],
            're_runnablepatrolhit': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_15',
            ],
            're_runnablepatrols1_cleared': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_24',
            ],
            're_runnableturretused': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_19',
            ],
            're_savebot_activate': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_13',
            ],
            're_savebot_complete': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_18',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.TroubleWithSpaceHurps.SeqEvent_RemoteEvent_18',
            ],
            're_sealdoors': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.BackOnSchedule.SeqEvent_RemoteEvent_2',
            ],
            're_showeastereggscore': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.EasterEggScore.SeqEvent_RemoteEvent_7',
            ],
            're_showoxygenmeter': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            're_spawnbotsforever_used': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_23',
            ],
            're_startfailsafetimer': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.BackOnSchedule.SeqEvent_RemoteEvent_3',
            ],
            're_startupbuttonfail': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.BackOnSchedule.SeqEvent_RemoteEvent_5',
            ],
            're_startupoverrideaborted': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.BackOnSchedule.SeqEvent_RemoteEvent_6',
            ],
            're_summonrunnablebot': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_17',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_18',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_29',
            ],
            're_takenonicedamage': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.InPerfectHibernation.SeqEvent_RemoteEvent_1',
            ],
            're_tassiter_voclear': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_15',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_21',
            ],
            're_tassiter_voclose': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_22',
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_6',
            ],
            're_tractor_beam_off': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            're_tractor_beam_on': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            're_updatedarcadescore_debris_1': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_6',
            ],
            're_updatedarcadescore_debris_2': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_7',
            ],
            're_updatedarcadescore_debris_3': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_8',
            ],
            're_updatedarcadescore_final': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_1',
            ],
            're_updatedarcadescore_meteors_1': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_12',
            ],
            're_updatedarcadescore_meteors_2': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_13',
            ],
            're_updatedarcadescore_meteors_3': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_5',
            ],
            're_updatedarcadescore_patrols_1': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_9',
            ],
            're_updatedarcadescore_patrols_2': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_10',
            ],
            're_updatedarcadescore_patrols_3': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_11',
            ],
            're_updatedrewardscore': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_4',
            ],
            're_vo_finished': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_16',
            ],
            're_vo_playing': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.Eradicate.SeqEvent_RemoteEvent_17',
            ],
            're_waterpipe_audio': [
                'InnerHull_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            're_workerbot_takedamage': [
                'InnerHull_Mission.TheWorld:PersistentLevel.Main_Sequence.DontGetCocky.SeqEvent_RemoteEvent_0',
            ],
            're_workers_on': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_60',
            ],
            're_workers_ready': [
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_55',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_56',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_57',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_58',
                'InnerHull_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_59',
            ],
        },
        'digsite_p': {
            'botsattoby': [
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            'camerafinished': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_40',
            ],
            'endsalute': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_10',
            ],
            'enterdigsitevo': [
                'Digsite_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'flaghoisted01': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_19',
            ],
            'flaghoisted02': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_36',
            ],
            'flaghoisted03': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
            ],
            'followbotwaypointattached': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_24',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_31',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_34',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_37',
            ],
            'guardianhunterkickoff': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'jackcallsloaders': [
                'Digsite_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
            ],
            'movetocherucorrosive': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
            ],
            'movetocherucryo': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_11',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_21',
            ],
            'movetocherushock': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_17',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
            ],
            'movetomoonp': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_14',
            ],
            'movetosarafire': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_23',
            ],
            'nearcaptainchef': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_9',
            ],
            'openguardianhunter': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
            ],
            'playcaptureddialog': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_32',
            ],
            'protectbots1spawners': [
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'protectbots1spawnersdead': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_15',
            ],
            'protectbots2spawners': [
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'protectbots2spawnersdead': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_38',
            ],
            'protectbots3spawners': [
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_3',
            ],
            'protectbots3spawnersdead': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_7',
            ],
            'start moving': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
            ],
            'stirwindialog01': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_13',
            ],
            'stirwindialog02': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_18',
            ],
            'stirwindialog03': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_20',
            ],
            'stirwindialog04': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_22',
            ],
            'stirwindialogbad': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_12',
            ],
            'thedonenemiesspawned': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_8',
            ],
            'zarpedon00': [
                'Digsite_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_1',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_28',
            ],
            'zarpedon01': [
                'Digsite_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_2',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_29',
            ],
            'zarpedon02': [
                'Digsite_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_6',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_30',
            ],
            'zarpedon03': [
                'Digsite_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_4',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_26',
            ],
            'zarpedon04': [
                'Digsite_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_5',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_27',
            ],
            'zarpedon05': [
                'Digsite_Audio.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
                'Digsite_P.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_0',
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_25',
            ],
            'returntohut': [
                'Digsite_SideMissions.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_35',
            ],
        },
    },
}
