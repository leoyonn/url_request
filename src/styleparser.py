#encoding=utf-8
'''
Created on 2012-8-16

@author: liuyang
'''
import re

def style_parse(file):
    scene_styles = dict({'正餐':set({}), '饮品':set({}), '小吃':set({}), '快餐':set({}), '西餐':set({})})
    lines = open(file).readlines()
    for line in lines:
        words = re.split('\s+', line)
        if len(words) == 1:
            continue
        style = words[0]
        for i in range(1, len(words)):
            if scene_styles.has_key(words[i]):
                scene_styles[words[i]].add(style)
    for k in scene_styles:
        print k,':',','.join(scene_styles.get(k))

style_parse('/home/liuyang/datas/food_style_scene.new')
