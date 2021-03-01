from collections import ChainMap

defaults = {'theme': 'default', 'language':'eng', 'showIndex': True, 'showFooter': True}
print(defaults)

cm = ChainMap(defaults)
print(cm)

cm2 = cm.new_child({'theme': 'bluesky'})
print(cm2)

print(cm2['theme'])

cm2.pop('theme')
print(cm2['theme'])

cm2.maps[0] = {'theme':'desert', 'showIndex': False}
print(cm2)
print(cm2.parents)
print(cm2['showIndex'])