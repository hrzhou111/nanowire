# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 08:58:45 2017

@author: zhr
"""
import numpy
import gdspy

def circle(diameter,width,pitch,total,half):
    i = 0        
    leftedge = []
    rightedge = []
    while i <= total:    #i=0，和total对应在x=0位置 
        leftedge.append((-numpy.sqrt(diameter**2/4-((half-i)*pitch)**2),
                         (half-i)*pitch))
        rightedge.append((numpy.sqrt(diameter**2/4-((half-i)*pitch)**2),
                         (half-i)*pitch-pitch+width))
        i = i+1
        
    return [leftedge,rightedge]

def circleiso(diameter,width,n):
    if n*width >=1:
         half_elecwidth = (n+4)*width
    else:
        half_elecwidth = 1
    length1 = float(diameter)
    radius = length1/2+2
    out_r = radius+1   
    angle =numpy.arcsin(half_elecwidth/radius)
    leftcir = gdspy.Round((0,0),out_r,inner_radius=radius,
                      initial_angle = angle+numpy.pi/2,
                      final_angle = numpy.pi*3/2-angle,
                      number_of_points=100,
                      max_points=100,
                      layer = 1,datatype = 1)

    rightcir = gdspy.Round((0,0),out_r,inner_radius=radius,
                      initial_angle = angle-numpy.pi/2,
                      final_angle = numpy.pi/2-angle,
                      number_of_points=100,
                      max_points  =100,
                      layer = 1,datatype = 1)

    return [leftcir,rightcir]
def circle_equ(diameter,maxdiameter,width,pitch,total,half):

    length1 = float(diameter)
    radius = length1/2+2
    out_r = radius+1
    leftpoints = []
    rightpoints = []
    i = 0
    while i <= total:    #i=0，和total对应在x=0位置 
        startpoint = (numpy.sqrt(out_r**2-((half-i)*pitch)**2),(half-i)*pitch)

        finalpoint = (maxdiameter/2,(half-i)*pitch-(pitch-width))
        rightpoints.append([startpoint,finalpoint])            
       
        startpoint = (-numpy.sqrt(out_r**2-((half-i)*pitch)**2),(half-i)*pitch)

        finalpoint = (-maxdiameter/2,(half-i)*pitch-(pitch-width))
        leftpoints.append([startpoint,finalpoint])
        i = i+1
    #return value[[[(,),(,)]],[[(,),(,)]]]
    return [leftpoints,rightpoints]  

def squire(diameter,width,pitch,total,half):
    i = 0        
    leftedge = []
    rightedge = []
    while i <= total:    #i=0，和total对应在x=0位置 
        leftedge.append((-diameter/2,
                         (half-i)*pitch))
        rightedge.append((diameter/2,
                         (half-i)*pitch-pitch+width))
        i = i+1
    
    return [leftedge,rightedge]

def squireiso(diameter,width,n):
    length1 = float(diameter)
    radius = length1/2+2
    out_r = radius+1 
    point1 = (-radius,-radius)
    point2 = (-out_r,radius)
    leftedge = gdspy.Rectangle(point1,point2,layer = 1,datatype = 1)
    point3 = (radius,-radius)
    point4 = (out_r,radius)
    rightedge = gdspy.Rectangle(point3,point4,layer = 1,datatype = 1)
    return [leftedge,rightedge]

def squire_equ(diameter,maxdiameter,width,pitch,total,half):   
    radius = float(diameter)/2+2
    out_r = radius+1   
    leftpoints = []
    rightpoints = []
    i = 0
    while i <= total:    #i=0，和total对应在x=0位置 
        startpoint = (-out_r,(half-i)*pitch)

        finalpoint = (-maxdiameter/2,(half-i)*pitch-(pitch-width))
        leftpoints.append([startpoint,finalpoint])            
       
        startpoint = (out_r,(half-i)*pitch)

        finalpoint = (maxdiameter/2,(half-i)*pitch-(pitch-width))
        rightpoints.append([startpoint,finalpoint])
        i = i+1
    #return value[[[(,),(,)]],[[(,),(,)]]]
    return [leftpoints,rightpoints]