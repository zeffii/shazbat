shazbat
=======

explorations in Kivy nodes

'futura'
node based geometry app for kivy.
Relies on Numpy and Python 3.4

MIT license (c) Dealga McArdle

Road map
=======


[ ] ---- Milestone 1

[ ] node definitions 1
  [ ] sockets
    [ ] key lists (edges, faces)  

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

  [ ] vector lists

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

  [ ] sliders 
    [ ] min, max, step (modifyable at runtime)
  [ ] bool 
  [ ] enum 
  [ ] node theme
[ ] move nodes
[ ] nodes connecting in / out
  [ ] wire types, themeable

[ ] nodes zoom
[ ] node list
  [ ] catagories [ ] icons
[ ] add nodes from list


[ ] ---- Milestone 2

[ ] node definitions 1
  [ ] box [ ] column [ ] row [ ] percentage row
[ ] node widgets
  [ ] graph [ ] tabbed graph [ ] color picker

[ ] slider node
  [ ] int
  [ ] float

