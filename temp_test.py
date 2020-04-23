# -*- encoding: utf-8 -*-
"""
@File    : temp_test.py
@Time    : 2020/4/23_18:09
@Author  : cousin liu
@Email   : 842076056@qq.com
"""

import pymel.core as pm


def create_follicle(p=None, n='follicle', g=None, u=0.5, v=0.5, t=False, r=False):
    u"""

    :param p: follicle's parent
    :param n: follicle's name
    :param g: geometry
    :param u: u value
    :param v: v value
    :param t: bool:connect translate
    :param r: bool: connect rotate
    :return: follicle
    """

    # 选择几何体
    if g is None:
        g = pm.selected()[0]

    # 判断父物体
    if p:
        follicle = pm.createNode('transform', p=p, n=n)
    else:
        follicle = pm.createNode('transform', n=n)
    pm.createNode('follicle', n=n + 'Shape', p=follicle)
    follicle.parameterU.set(u)
    follicle.parameterV.set(v)
    # follicle.getShape().v.set(0)
    # mesh 类型 outMesh关联inputMesh
    print 1
    if g.getShape().type() == 'mesh':
        print 2
        g.outMesh.connect(follicle.inputMesh)
    # 其他的（曲面）local 关联 inputSurface
    else:
        g.local.connect(follicle.inputSurface)

    # 判断是否连接translate
    if t:
        follicle.outTranslate.connect(follicle.translate)

    # 判断是否连接rotate
    if r:
        follicle.outRotate.connect(follicle.rotate)
    follicle.inheritsTransform.set(0)
    print follicle
    print 'Typ:__', type(follicle)
    return follicle


# create_follicle(p = None, n = 'follicle', g = None, u = 0.5, v = 0.5, t = True, r = True)

def selected_obj():
    sel = pm.select('loftedSurface1')
    # print sel.getShape().type()


# selected_obj()

def set_matrix_loc(n='Loc', number_loc=0):
    prefix = 'sec_Ctrl'
    for i in range(number_loc):
        pre = '{prefix}_{i:0>2}'.format(prefix=prefix, i=i + 1)
        u = (1.0 / (number_loc - 1)) * i
        follicle = create_follicle(g=selected_obj(), n=pre + '_follicle', u=(1.0 / (number_loc - 1)) * i, v=0.5, t=True,
                                   r=True)
        # pm.select(cl = 1)


set_matrix_loc(n='Loc', number_loc=3)

