shazbat
=======

explorations in Kivy nodes

'futura'
node based geometry app for kivy.
Relies on Numpy and Python 3.4

MIT license (c) Dealga McArdle

Road map
=======

```

[ ] ---- Milestone 1

  [ ] bool 
  [ ] enum
  [ ] layout
    [ ] box 
    [ ] column 
    [ ] row 
    [ ] percentage row
  [ ] sliders 
    [ ] min, max, step (modifyable at runtime)
  [ ] node theme
    [ ] wire types, themeable
  [ ] move nodes
  [ ] nodes zoom
  [ ] node list
    [ ] categories 
    [ ] icons
    [ ] add nodes from list

[ ] ---- Milestone 2

  [ ] sockets
  [ ] nodes connecting in / out  
  [ ] key lists 
    [ ] edges
    [ ] faces
  [ ] vector lists
  [ ] node widgets
    [ ] graph 
    [ ] tabbed graph 
    [ ] color picker

[ ] ---- Milestone 3
  
  [ ] slider node
    [ ] int
    [ ] float

```

SocketTypes
======

edges, faces

``` 
key_dict = {
    'type': {'edges','faces'}
    'data_faces': [
        {'faces': [[....]]}, 
        {'faces': [[....]]}
    ],
    'data_edges': [
        {'edges': [[....]]}, 
        {'edges': [[....]]}
    ]
}
```

verts

```
vec_dict = {
    'type': {'vec3','vec4'}
    'data_vec3': [
        {'vec3': [[....]]}, 
        {'vec3': [[....]]}
    ],
    'data_vec4': [
        {'vec4': [[....]]}, 
        {'vec4': [[....]]}
    ]
}
```
