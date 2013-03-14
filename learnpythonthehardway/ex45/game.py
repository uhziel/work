#!/usr/bin/env python2

import scene

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        cur_scene = self.scene_map.start_scene
        while True:
            next_scene_name = cur_scene.enter()
            if next_scene_name == "finished":
                break
            else:
                cur_scene = self.scene_map.get_scene(next_scene_name)

class Map(object):

    scenes = {
            "death" : scene.Death(),
            "central_corridor" : scene.CentralCorridor(),
            "laser_weapon_armory" : scene.LaserWeaponArmory(),
            "the_bridge" : scene.TheBridge(),
            "escape_pod" : scene.EscapePod(),
    }

    def __init__(self, start_scene):
        self.start_scene = self.get_scene(start_scene)

    def get_scene(self, scene_name):
        return Map.scenes[scene_name]

scene_map = Map('central_corridor')
engine = Engine(scene_map)
engine.play()
