#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import exit
from random import randint


class Engine(object):    
    
    
    def __init__(self, scene_map):
    	
        self.scene_map = scene_map
    
    def play(self):
    	
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('the_end')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()
    
    
class Scene(object):     


    def enter(self):
        print "not configured yet"
        exit(1)  

	
class Start(Scene):
    
    
    print "Enter your name: "
    name = raw_input(" ")
    print "Your name is %s" % (name)
	
    print "Hi %s. How old are you?" % (name)
    age = int(raw_input())
    print "You're %r years old" % (age)

    def enter(self):
    	
        if Start.age < 18:
            print "Sorry %s... You're too young to play this game." % (Start.name)
            return "the_end"
        
        elif Start.age >= 18:
	        print "Excellent %s! We can continue! Press enter" % (Start.name)
	        raw_input()
            
        print """Ok %s...
        I can tell you that it's not a comfortable situation.
        You've lost your memory so here's what happend.
        Today you were eating breakfast on your terrace and suddenly some alien showed from nowhere.
        It has minimized you with its odd gun so now your size is like a match box - more or less.
        Furthermore, the alien has teleported you - you are in some unknown empty house.
        You have to get yourself out in order to come back home, find the alien
        and bring back your initial size.""" % (Start.name)
        raw_input()
        return "corridor"
        

class The_end(Scene):
	
	
    def enter(self):
    	
        print "you're dead"
        exit(1)


class Corridor(Scene):
	
	
    def enter(self):
    	
        print """Your're in the corridor. You're thinking 'hmm... how can I escape this f... house'
        You can see a main front door, it is metal and locked so there is no way to leave through it.
        You can also see 3 other doors open. There is a kitchen (1), bathroom (2) and living room (3).
    
        Where do you want to go? Choose the number."""
    
        room = int(raw_input())
    
        if room == 1:
            print "You're going to kitchen"
            return "kitchen"
        elif room == 2:
            print "You're going to bathroom."
            return "bathroom"
        elif room == 3:
            print "You're going to living room"
            return "living_room"
        else:
            print "That's not an answer. Try again."
            return "corridor"


class Kitchen(Scene):
	
	
    def enter(self):
    	
        print """
        
        Ok, so what can you see in the kitchen... there is a total mess but no window,
        no balcony, nothing interesting honestly. There is no way to escape by kitchen
        so you have to go back to the corridor. You turn around and there is a spider on your way.
        It is much bigger and faster than you so you don't have any chance to kill it or even run away.
        Surprisingly the spider can talk. It says:
        
        "Hello bro. What do you want?"
        Your answer:
        
        """
        
        raw_input('')
        
        print """
        
        bla bla bla... You cannot go back to the corridor unless you answer 3 questions correctly.
        If you don't, I will kill you, that's my house.
        
              
        
        """
       
        print "How many legs do I have? (the spider starts to dance so it's difficult to count legs)"
         
        answ1 = int(raw_input())
        if answ1 == 8:
            print "Correct. Next one."
        else:
            print "You're kidding me? I'm gonna eat you"
            return "the_end"
        
        print "I'm a male fowler. How many years do we approximately live?"
            
        answ2 = int(raw_input())
        if answ2 in range(3,6):
            print "You lucky bastard. Next one."
        else:
            print "You're too stupid to live."
            return "the_end"
           
        print "What is green and jumps?"
        answ3 = raw_input('')
        print """No, it's not a %s. It's a soldier at the disco. But your answer was not so bad. You can go.
        
        
        
        """ % (answ3)    
     
        return "corridor"


class Bathroom(Scene):
	
    def enter(self):
    	
        print "Ok, there is a shower so you can eventually jump into the sewage system. Do you want to do that?"
        jump = raw_input('')
        if jump == 'yes':
            print "You get drowned in a sewage system."
            return "the_end"
        else:
            print "There's nothing else to do so you go back to the corridor."
            return "corridor"


class Living_room(Scene):
	
	
    def enter(self):
    	
        print """What do we have here? Bed, wardrobe...
        oh! it's computer, excellent!!! It's open and turned on.
        But you have to enter the password...
        Oh there is a piece of paper with passowrd next to the computer!
        It starts with "sth12" but there are 2 digits left that you have to guess.
        Ok, let's try!"""
        
        first_part = "sth12"
        second_part = str(randint(0, 9)) + str(randint(0, 9))
        password = first_part + second_part
        guess = raw_input('')
        
        while password != guess:
            print "The password is not correct. Do you want to try again?"
            ans = raw_input('')
            if ans == 'yes':
                guess = raw_input('')
            elif ans == 'no':
                return "corridor"
            else:
                print "That's not an answer."
        
        print """
            Excellent! You entered the correct password.
            Now you can contact your wife via facebook and she will let you out.
            Congratulations!"""
        raw_input()
        exit(1)
            
        
class Map(object):    
	

    scenes = {
	"start": Start(),
    "corridor": Corridor(),
    "kitchen": Kitchen(),
    "bathroom": Bathroom(),
    "living_room": Living_room(),
    "the_end": The_end(),
	}
    
    def __init__(self, start_scene):
    	
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
    	
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
    	
        return self.next_scene(self.start_scene)
   
a_map = Map("start")
a_game = Engine(a_map)
a_game.play()
