
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMARESTAleftMULTIPLICACIONMULTIPLICACION NUMERO RESTA SUMAexpresion : expresion SUMA expresion\n                 | expresion RESTA expresion\n                 | expresion MULTIPLICACION expresionexpresion : NUMERO'
    
_lr_action_items = {'NUMERO':([0,3,4,5,],[2,2,2,2,]),'$end':([1,2,6,7,8,],[0,-4,-1,-2,-3,]),'SUMA':([1,2,6,7,8,],[3,-4,-1,-2,-3,]),'RESTA':([1,2,6,7,8,],[4,-4,-1,-2,-3,]),'MULTIPLICACION':([1,2,6,7,8,],[5,-4,5,5,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,3,4,5,],[1,6,7,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expresion","S'",1,None,None,None),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_binaria','main.py',44),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_binaria','main.py',45),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_expresion_binaria','main.py',46),
  ('expresion -> NUMERO','expresion',1,'p_expresion_numero','main.py',55),
]
