## Head Tracking

```
In this video, we will continue talking about VR hardware. 
In particular, we will focus on head tracking. 
First of all, as mentioned in the previous videos, 
we tracked the user's head in order to 
update the displays according to the user's viewpoint. 
It's important we can do it very quickly to maintain emotion. 
Most VR devices on the market have 
this tracking latency controlled at level of single digit milliseconds. 
So it's not noticeable in most cases. 
There are other processes in this procedure that could 
cause further delays in updating the graphics, 
but they are independent of the tracking technology we're talking about here. 
And we will discuss those other factors later in the course. 
Secondly, we need to track the user's viewpoint in the 3D space. 
This implies we have to track their head rotation and position. 
In the CAVE, there are normally built-in systems in 
the small tracker which the user wears on top of their shutter glasses. 
The built-in tracking system tracks 
the user's head rotation using accelerometer or gyrometer or both. 
They can be very tiny and the same methods are actually used in 
most smartphones in order to support 
features such as autorotation when you flip your phone like this. 
For position tracking, external optical tracking devices are normally used. 
In the CAVE, it could be several ceiling-mounted infrared cameras pointing at 
a user so they can calculate the position of the user in 
the 3D space and feed the data to the machine, 
which then takes care of updating the display accordingly. 
Here, how you mount the cameras is important as this defines the range of capturing. 
So when you come outside of the CAVE or come very close to one of the walls, 
you might lose position tracking as not all cameras can see the head tracker. 
The same applies to HMD head-tracking. 
We would need to use built-in accelerometers and gyrometers to track 
the user's head rotation and external optical devices to track their head position. 
In this case, the external infrared sensor 
is mounted in front of the user as you can see here. 
And again, the range of capturing depends on how the sensor is set up. 
If the sensor is set up in front of you and you move 
away to a place where the sensor can no longer see you, 
then we lose position tracking, 
which means the graphics can no longer update according to your viewing position. 
It is important to mention that not all devices come with position tracking. 
Some have rotation tracking only. 
This means that you can still look around but you are stuck where you are. 
You won't be able to move around in VR with your body to get closer to 
certain objects or observe them from a different angle like you can in real life. 
You can still navigate the 3D environment with a controller, 
a touchpad or joystick, 
but it won't be as natural, 
and you won't have a good sense of scale in VR without this position tracking. 
In fact, none of the mobile devices currently on the market come with position tracking, 
be it Google Daydream or Samsung Gear VR. 
It's normally a HMD box for you to slot in your smartphone, 
and they don't come with 
external optical tracking sensors like the high-end HMD devices do. 
Part of the reason for this is that mobile VR 
is very much about their unsophisticated setup, 
and that you can move freely in a room without out of range problems. 
So it's against the design principles to add 
a sensor which will then bring new constraints. 
Also, integrating position tracking and updating the graphics in 
real time potentially could consume a lot of computational power, 
which is more difficult to support with just a mobile phone. 
There are possible technical solutions to track the position of the HMDs 
without relying on external position tracking devices. 
For instance, a technology called 
self-tracking or inside-out tracking has had some success. 
It is beyond the scope of this course but you're free to read about it. 
It's basically still a challenging problem in machine vision. 
You might get it to work in certain conditions, 
but it might not be robust enough to work in 
everyone's living room with their own personal lighting conditions. 
At the time of recording, 
I have not seen a consumer-oriented VR headset that comes with robust position tracking, 
but this might change quite quickly over time. 
It is something to watch out for before buying your VR device. 
It is possible in the near future we will have wireless HMDs 
powered by desktop machines, for instance, Bluetooth. 
So users are free from the constraints of 
cables yet benefiting from a very powerful machine, 
which enables sophisticated graphics and 
interactions beyond the computational power of a mobile phone. 
```



## Controllers

```
[MUSIC] 
By now you should have had a good overview of how VR display works and 
how it supports immersion. 
In this video, 
we will move on to another component of VR hardware, the VR controllers. 
Again, let's start with the cave. 
What this user is holding in their hands is something called a VR controller, or 
we often refer to it as the wand. 
In VR, you will be interacting with objects using these wands, 
picking up and moving objects, or 
when you're talking with a friend pointing at something, or gesturing. 
In order to pick up an object in the 3D space, 
the system will need to know where your hands are. 
So we will need to be able to track the position of the wand. 
In the real world, if I like to grab my mug to see if I still have tea in it, 
I will have to rotate the mug slightly. 
So in VR, I should also be able to do this, 
which requires rotation tracking of the wand. 
The same thing applies to communication functions. 
If both the position and rotation of my hands are tracked, so 
with a wand, I will be able to use gestures to communicate to some extent. 
So essentially, we need to track the position and rotation of the wand. 
This is done exactly the same way as head tracking. 
The wand itself has a built-in system to track rotation and 
it uses external optical sensors to track it's position. 
Other than interacting with objects and gesturing with friends, often the wand 
is used for something we don't normally do with our hands in real life. 
That is navigation. 
Basically, we can use the wand to walk around 3D world without moving 
the actual position of our body. 
This enables users to explore a virtual world that is bigger than the physical 
space they're actually in. 
The methods for navigating the 3D world without having to move your 
body often come from our experiences in video games with a 2D user interface. 
In order to look and move around in a video game, 
we often use a touchpad, mouse, keyboard, or joystick. 
A similar method has been adapted for us to navigate in VR. 
As you can see in the middle of the wand, 
there is a small joystick which you can use to navigate your 3D environment. 
When you use the joystick to move around in VR, 
it can be called virtual navigation, as opposed to 
actually moving around in the physical navigation of the real life. 
But there are many other ways in which 
you can use a wand to navigate in VR without using this joystick. 
And these methods are often more natural and less likely to cause nausea. 
We will talk about these navigation methods and 
nausea in VR later in this course and the other courses in our VR specialization. 
The VR controllers used in high end HMDs are very similar 
to the ones used in the cave. 
They're both rotation and position tracked. 
And they often come with a joystick or touchpad in the middle for navigation. 
Furthermore, most VR controllers nowadays 
are able to provide haptic feedback through vibration. 
So, what does this haptic feedback through vibration mean? 
In real life, when I put this mug on the table 
I will feel a small vibration the moment the mug touches the table. 
This can be supported by the controller in VR. 
Because we have the position tracking of the wand, the system knows where the mug 
is moving in a 3D space, and it knows the 3D position of the table. 
So when these two overlap with each other in the 3D space, at the moment the mug 
touches the table, the system can detect it and make the controller 
generate a small vibration to resonate with what I expect to feel in real life. 
This gives a very strong sense of immersion. 
This illusion is so 
strong, I have seen various cases of people who after spending some time in VR, 
putting virtual objects on a table that doesn't really exist, were so convinced 
subconsciously that there was a table, they would lean against it and fall. 
For myself, there were a few times I almost left the VR controllers on 
the virtual table because I forgot that it didn't really exist. 
Fortunately, I have never dropped and broken one so far. 
Another point I would like to mention is that when our uses try to move around 
using the joystick and touchpad, which is something we call virtual navigation, 
it's more likely someone would feel nausea in the HMDs than in the cave. 
So you are encouraged to find other ways to navigate the 3D space rather than just 
importing a first person controller normally designed for a 2D user interface. 
Again, we will talk more about this later in this course. 
Finally, when it comes to mobile VR systems, 
only some of them come with a controller. 
But the position of the controller is not normally tracked for 
the same reason we discussed with head tracking. 
Also, they don't usually have built-in mechanisms to provide vibration feedback. 
Google Daydream comes with a controller, 
with a touchpad which provides rotation tracking. 
Samsung Gear VR has a touchpad on the right hand side of the HMD. 
[MUSIC] 
```


## Oculus Rift

```
This is the Oculus Rift CV1. 
This is the first commercial release of the Oculus headset. 
It is a very light plastic construction. 
It has adjusters, Velcro adjustments for any head. 
It has two inside lenses, 
which we can also just to fit any shape of head, 
has built-in headphones, hardwired connected to a computer. 
It can track in two ways. 
It has inbuilt sensors that allow the rotations of your head from the neck up. 
And then it also has ability to track position in space so we can move forward, 
move back, walk around, duck, 
weave in order to play games. 
When buying that, it comes as a pack with this section here. 
Inside that, you will receive one positional tracking camera. 
You also get a 360 Xbox controller 
with its wireless dongle and the Oculus Rift remote pointer, 
which is just a simple interaction for many navigations. 
So, having purchased the Oculus, 
you can expand it with what's called the Oculus Touch package. 
Inside that, you'll find another positional tracking camera, 
which we use in tandem to create a bigger tracking and play space. 
It also comes with, 
what's called, the Oculus Touch controllers. 
Now, these separates our hands into individual hands in VR. 
They have some common components, which we use to, 
such as joysticks, buttons and triggers. 
However, these controllers are positionally tracked, 
most importantly, as differs to the pointer and the game controller. 

HMD
HTC Vive
Hi, I'm going to take you through the HTC Vive setup, 
which breaks down to head-mounted display, two lenses inside. 
Essentially It's a mobile phone display in there. 
HTC best known for making mobile phones but 
they've moved very heavily into the virtual reality area now. 
And there's a high definition display and two handsets, 
controllers on the back triggers, buttons, etc. 
These are your hands in the virtual world. 
And all of these are tracked very exactly in a 3D space, and 
they do that using these lighthouse units. 
These emit a vertically spinning infrared laser and 
horizontally spinning infrared laser. 
Each of these devices is covered in sensors that sees the vertical and 
the horizontal beams and sends that back initially from the handsets, 
Bluetooth to the headset and from the headset down the cable to your computer. 
The positional information is then translated into a rendered image in 
the computer, which goes back up into the headset. 
So as you move around your view stays with you. 
The lighthouse unit you position them anywhere between two meters, 
ideally five meters or just a bit more apart. 
And that creates a 3D space that you can move around in at will. 
And you're fully tracked. 
None of the other systems really do this. 
And legend has it that you'll be able to add on more modules, more rooms. 
So you can move seamlessly between room to room in your virtual reality. 
The one thing to remember about the Vive unit is it doesn't have 
the sound built in like the Oculus. 
So you got to put some headphones on as well. 
And you got to put the headphones on after the headset, and 
then take the headphones off first, otherwise you get all tangled up in wires. 
This is the junction box, and here we have HDMI for the video. 
We've got a USB for the positional sensing, and 
we've got a 12-volt power supply which stabilizes the whole system. 
What it means is that the HDMI and USB go into your computer, 
And then you've got an additional plugin 12-volt power supply. 
Finally, we've got this little junction box here. 
And what this does is that it takes your HDMI for the video, the USB for 
the position sensing, and an additional 12-volt power supply, 
which stabilizes the whole system. 
So that needs to be plugged into the wall, while the other two go into your computer. 
And again that's your HTC Vive. 
[MUSIC]
```

## Sony PlayStation VR

```
Hi, I'm Dave and this is Isabel. 
And we are going to tell you all about this stuff that you 
need to use the PlayStation VR headset. 
So first thing you need, obviously, is the headset. 
So, the PlayStation VR headset, feeling it, 
it's actually the heaviest one out of all the ones you can buy, 
but it's actually most comfortable. 
So as you can see here, it's got all the padding in here like the cushioning, 
but it also is really good at adjusting to fit different people's heads. 
So, there's a button on the back right here, when you press it in, 
you pull it forward like that, and then, 
it's adjustable, and they're big enough to fit over Dave's head. 
Thanks. 
You'll also see that there are these blue lights right at the back here. 
When it's on, the blue lights appear on the front of it, 
and these lights actually used sort of trackers, right? 
To be picked up by this stereo cameras. 
Well, do you want to talk a little bit about the weight distribution? 
Yeah. Well, the interesting thing is, 
I think because Sony had been so experienced at making 
things like headphones and other electronics, 
they've done a great job of the weight distribution too, as Isabel said. 
Although it's the heaviest, they actually, 
it feels like the lightest. 
And the other thing to say is these trackers, 
when they get tracked by this camera, 
that gives us full positional tracking. 
So not only do we know which way it's rotated, 
we also know where you are in space, 
which is different to their current mobile setups 
where they just know the rotation of the headset. 
So the main thing you need to power the PlayStation VR headset is the PlayStation 4. 
It also comes with this box as well, 
which is the power but it also splits up the signal between the headset, 
and the PlayStation, and the TV. 
One last thing about it is that you can plug in your own headphones on the side here, 
there's a lot of control panel with the volume controls, 
and also it's way you turn on/off the headset. 
And as well as Isabel said, 
you can plug in your own headphones on this box. 
Not only does it do the visual video splitting, 
but it also does all the calculation for the sound, 
so it can place it all around you in 3D. 
You can do some experiences just with the headset, 
but also, you can use controllers. 
So this is a traditional game controller. 
It's the standard PlayStation DualShock 4. 
This has gyros in it and that means again, 
you know the orientation of it, 
but you don't know exactly where it is in space. 
It does have this light bar, 
and that can be tracked by this camera. 
But as soon as, 
so you can imagine it like that, as soon as you go out like that, you lose that tracking. 
So it's that limited what that can do. 
It has a bunch of buttons on it, 
these classic PlayStation buttons, 
and this D-pad, and then, 
these two joysticks, and even has these shoulders as well. 
So this is great for playing all kinds of games, 
but it can be a bit limited in VR because you really want to have hands. 
And that's where these guys come in. 
So these are PlayStation Move controllers. 
They were actually released about 10 years ago, 
way before any VR was happening. 
And as motion controllers, 
similar to the Nintendo Wii controllers, 
and when these are on, 
these ping pong balls glow different colors, 
and again, the camera can track them. 
So altogether, the camera and the processing of that feed 
has got a lot of work to do because it's going to track these lights on from the headset, 
and track these as well. 
These have the same gyros in this, 
so we have some orientation. 
And then, with these glowing ping pong balls, 
we actually get very precise information the way your hands are. 
Using these triggers that are on them, 
we can then replicate what it's like to pick things up, and at that point, 
you get some really great VR experiences because not only are you in full VR, 
you've got great 3D sound, but then, 
you've got hands as well, 
and that feels very very natural, and very intuitive. 
And so, I think that's one of the big benefits of the high-end systems now. 
They've got these hand controllers if you like, 
but you can tell from these, 
they've got these tiny buttons on the front which is 
unlike any of the other hand controllers for VR. 
And that's because they were originally 
designed where they thought you'd be able to see them, 
but now you can't because you're in VR. 
So, I wouldn't be surprised if they 
redesign them at some point to make that a bit clearer. 
```

## Mobile VR | Google Cardboard and Samsung Gear

```
Now we're going to go for mobile phone VR. 
There's quite a range of options. 
What I've got here is the Samsung Gear VR, 
which only works with their phones, 
and it's got some extra bits and bobs, 
a little trackpad on the side and menu keys and so on. 
What I've got here is really the most easy access and affordable VR, 
which is the Cardboard. 
It has two lenses inside it just like all the other headsets but essentially, 
other than that, it's a cardboard box. 
It's just one of many types. 
You got all sorts ranging from things you print out on the Internet and simply cut out. 
This one is the higher end audio mobile phone VR. 
Again, there's disadvantage and advantages. 
The resolution on it is pretty comparable to one of the major handsets, 
but you've got a lot less functionality. 
You've got an app in here, 
the switch on, and then very carefully, 
as it popped in there, 
and you can now look in it to be like that, 
and you're in a VR environment. 
Again, it's quite high resolution, it's pretty good. 
And the key thing to realize with this, 
is that there are millions of them. 
The market in terms of the high end machines like the Vive, 
the Oculus is in a few hundred thousand. 
There's millions of these so if you want to develop games in VR, there's a market. 
Would you like to tell us more about the? 
Obviously, the cardboard is very affordable access way into VR. 
It essentially offers you much the same as the Gear VR, 
missing a few buttons and controls. 
It's actually very minimum but just like Gear VR, 
it needs any mobile phone for this not specifically Samsung. 
It has two lenses in it, just like the high end headsets. 
It goes in, you position it in front of 
the lenses and simply vault a great shot and on it guys, 
and I can then involve myself in VR just the same 
way as anyone else really for very little money at all. 
It's important to say I think at this point that this contain 
no positional tracking so one limitation 
we do have is that it only manages our rotational information from accelerometers. 
We do not have the positional tracking that we do in Vive and Oculus. 
I mean that's the key thing that's not here. 
In this one got little joypad on the side but it remains 
a single camera at the center of a ball of video. 
And you must really always bear in mind these limitations. 
As a developer of VR, 
I'd say that you know your target, 
and you develop games that are sensible for that. 
```

## CAVE VR System

```
[MUSIC] 
Hi, I'm David Swomp, I am the manager of the immersive Virtual Reality Lab here at 
the University College London. 
And I'm just going to show you our cape facility. 
This is a four-wall projected VR facility, 
a bit of a contrast to head-mounted displays in a number of ways. 
So, crucially the difference here is, 
instead of making you wear the displays, we just project an environment around you. 
So you can see an environment here. 
It's a room, it has some furniture in it, tables, chairs, 
a clock on the wall, that kind of thing. 
And the people not wearing the set can see it. 
So although it is still a single person, a single user 
facility, more than one person can see the environment in here. 
The way it works, three of these walls are back projected, 
which means they don't cast a shadow, the projections come from behind the wall. 
The floor is projected from above, just because we don't have room here to 
back project it, it's the only one that casts a shadow, casts is slightly back so 
people tend not to see it. 
For the 3D, we have these tracked active stereo glasses. 
Now what I mean by active stereo is instead of using the polarizing 
technology that you might get with 3D cinema where you have two projectors, 
different polarizations, we use a single projector for each screen. 
And they alternately put out a left eye image and 
a right image very, very quickly at 100 frames a second. 
What these glasses do, 
they have liquid crystal lenses that alternatively block out the left and 
then the right eye, so that each eye only sees the appropriate view. 
As well as that, of course, they have to display a perspective correct view. 
So for that the glasses are tracked. 
so you'll see as I move them around, 
we get a different perspective view from the floor down there. 
So the person wearing these has a perspective correct view of 
the environment all the time. 
The other aspect of this of course, 
is that the person needs to have accurate perspective of the world. 
And for this we need to have tracked point of view for each of the eyes. 
There are lots of different ways you can do this tracking of course. 
Here we have camera based optical tracking. 
So the six cameras you see around here with the red LEDs, 
they're bathing this environment in near infrared light. 
And the near infrared cameras are picking up the positions of these 
retro reflective markers. 
They're arranged in a pattern that you can recognize. 
So from the six different views, you can very accurately get the position and 
orientation of this in space. 
And that information is fed back to the computer and 
it will draw from the correct orientation. 
So this differs from normally, say, 
if you were just setting up 3D graphics on a desktop computer. 
You'll set up your camera to have a viewing frost that see 40 centimeters in 
front of the screen, and everything will look about right. 
Here, we've got eight different viewing frost, one for 
each eye for each of these screens, and they're constantly changing shape. 
So these off-axis projections that all have to be calculated for 
every frame as it changes. 
So you can see how the point of view moves through the scene, 
if I put this down on the floor, we have a view from the floor. 
We also have, for interaction, another tract device. 
You can have as many of these as you like. 
You might have, if you want to do full body motion capture, 
you would put these markers and a motion capture suit all over your body. 
Here, we've just got a tracking device that's tracking the position of my hand, 
so you can see this pointing device here. 
It also has some buttons on it, so we can program them to do different things. 
In this environment we programmed it to allow it to unlock this box, 
and open the lid of it. 
But you might use it for navigation, for 
selecting objects, for making things happen. 
Just depending on the application you have. 
One of the main contrasts with headmount displays, and 
this is a consequence of not wearing the displays, is here we're capable of 
providing a much wider field of view than you'll get with a headmount display. 
Typical head-mounted displays that you have now will go between 100 and 
120 degrees field of view. 
In here, if you stand in the middle, you have 270 degrees horizontal field of view. 
Of course, head-mounted displays will give you a complete range of view, 
no matter where you look, you're looking at the environment. 
In here just because of the design of this, if I look up I'm looking out at 
environment, if I look back this way, I'm looking out of the environment. 
Another consequence of this is that you can get away with 
lower frame rates in here. 
With the head mount display you really want to be running minimum 60 hertz. 
Probably 90 hertz to have smooth looking graphics as you look around. 
In here because you're not wearing it, when you do, especially rotations, 
turning your head, what you're going to look at is already there. 
So you have some, a greater tolerance for lower frame rates in here. 
Another consequence of projection setups goes to head mounted displays is here. 
You can see your own body. 
So when I look around in here I can see my own hands. 
This is, depending on your application, this can be an advantage. 
Sometimes the head mounted displays it's better not to be able to see your 
own body. 
So for example, if you have a virtual body, an avatar, 
obviously you have the overhead of having to create that and having to track that. 
On the other hand, if you want to do interactions with virtual objects, 
it's very much easier to trick people into thinking that the positioning is accurate. 
The overhead of doing it when you can see your real body and 
track them with virtual objects is far greater. 
You also enter into what we call accommodation vergence problems. 
So for example, if I look out here and I'm looking at the edge of this table here. 
To me, this looks like my hand is in the same place as it. 
However, if I look at it, I can't quite focus on both my hand and the edge of 
the table at the same time, because physically they're at different distances. 
So having said that this is a single user experience, only one person can be 
wearing a tracked pair of glasses and getting the correct perspective hue. 
You can, of course, have small groups of people in here. 
They can wear the stereo glasses. 
And if they stand near to the person being tracked, 
they will have an almost perspective correct view. 
This is quite good for things like designer view and engineering or 
architecture ,where you might have groups of people who want to talk to each other. 
And of course, 
they don't have the isolation of wearing head-mounted displays. 
They can see each other in here. 
One other aspect that impacts in different ways, 
is the problem of simulator sickness. 
This effects all modes of virtual reality, head mount displays and caves. 
In here, you have the advantage on one hand that because you're not 
wearing the screens, you can cope better with the latency of rotation. 
So that you don't get this big wash of graphics when you turn your head, 
which can be quite disorienting, especially if there's some latency there. 
On the other hand, you also have a very, very wide field of view. 
So you get that stimulation to the periphery 
of your eye where all the motion sensitivity is. 
So actually, when you do a lot of navigation in here, 
you can make motion sickness problems worse. 
So again, 
this comes down to good application design to avoid these problems. 
[MUSIC]
```

## Windows Mixed Reality

```
Windows MR (as it is often called) was released by Microsoft in Autumn 2017, and it is built into the latest version of Windows 10. It is an open platform in the sense that anyone can develop a headset. This is similar to Microsoft's normal strategy, they don't develop proprietary computers (like Apple) but build a platform (Windows) that can be used by many hardware developers. They have worked with a number of hardware companies who have released headsets, which you can see below:
Windows MR is a 6DOF platform that supports both rotation and position tracking in the headset as well as two position tracked controllers that are similar to the HTC VIVE controllers or the Oculus Touch. One of the biggest innovations is that it uses inside-out tracking. The position tracking is done using cameras on the front of the HMD, not external cameras. This makes the set up a lot easier. 
Windows MR head sets have very similar capabilities to other high end VR headsets like the Oculus Rift and HTC VIVE and it is a good third option for high end VR. 
```

```
For example, we have tested the ACER Mixed Reality Headset, which features an innovative design, but otherwise feels very comparable to the Rift and VIVE.
```
### REFERENCE
1. https://medium.com/virtual-reality-virtual-people/windows-mixed-reality-and-oculus-go-745ef6e31760
1. https://medium.com/virtual-reality-virtual-people/acer-and-windows-mr-7e9247218aca
1. https://medium.com/virtual-reality-virtual-people/acer-windows-mixed-reality-hands-on-9ac9122d508b



## Oculus Go

The Oculus GO is a mobile VR platform that is very similar to the Samsung Gear VR (in fact they can run exactly the same software). However, it is completely stand along, it does not need a mobile phone to be inserted into it, all the hardware is in the HMD. 


That makes it a very cheap and easy way to get into VR. At $100 it is a bit more expensive than the Gear VR, but you don't need to buy an expensive Samsung phone. That means it is likely to be a a popular gateway to VR. 


However, as a mobile platform, it is less capable than a high end VR platform, and in particular does not support position tracking. 
https://medium.com/virtual-reality-virtual-people/oculus-go-hands-on-e7a279dc47e8

## Oculus Quest

The Oculus Quest is a stand alone mobile VR platform. That means that like the Samsung Gear VR, it does not have to be connected to a computer, and unlike the GearVR it does not even need a mobile phone. 

However, it is unlike the mobile VR platforms discussed in the course. That is because it is the first mobile VR headset to implement the innovation that Sylvia predicted: Inside out tracking. That means that it can do position tracking (and therefore 6DOF) of the headset without the external cameras used by the Rift and VIVE, but with cameras on the HMD itself. This also allows it to have tracked 6DOF hand controllers. 

This makes it the equivalent of what we have called "High end VR" but in a mobile package. That is quite a breakthrough and we think it will have a big impact on the VR industry. 
https://medium.com/virtual-reality-virtual-people/oculus-quest-development-in-unity-b3bac62fda87
VR Apps can be downloaded from

## Oculus Rift:

https://www.oculus.com/experiences/rift/

## HTC VIVE:

http://store.steampowered.com/

## Sony PlayStation VR
- Games: https://www.playstation.com/en-gb/explore/playstation-vr/games/ 
- Experiences: https://www.playstation.com/en-gb/explore/playstation-vr/ps-vr-experiences/ 
- Gear VR: https://www.oculus.com/experiences/gear-vr/

## VR in Analogue Age

Although most people have tried virtual reality only quite recently, 
the technology of VR has existed for a few decades. 

I thought, who would be in a better position to tell you all about the history 

of VR than Proffesor Anthony Steed? 

Who was awarded the 2016 VGTC VR Technical Achievement Award. 

So it's my great pleasure to have Anthony here. 

```
>> Hello, I'm head of Virtual Environments and Computer Graphics in the Department of Computer Science at the University College London. I got started in virtual reality research in late 1992.
So it's my pleasure to give you a short history of virtual reality. 
And one of the difficulties in trying to present this in a short format is that you can have quite long discussions about how long the history of virtual reality is. So I'm going to start off with some things which are quite old, and refer back to sort of the history of creative arts and media and theater, and so on. So this image here appears to show a violin hanging on a door, and 
it's in a stately home. You can go and visit this, it's the stately home called Chatsworth House, which is in Derbyshire in England. And what you see is a very convincing looking violin hanging on the door, 
but it's an illusion, trompe l'oeil. It's a painting done in a manner which convinces you that there is a violin hanging on the wall. 
And these types of image were very very popular in the 1600s, 1700s. 
This one is by Jan van der Vaart. And he learned the technique after visiting Italy, where they were popular tourist attraction for rich families. 
But what we can see here is sort of the start of some of the features that we now see in digital virtual reality. In particular this violin has been painted in such a way that it appears to have all the shadows and lighting that come from the real environment around it. 
And it's quite striking that it appears to be stood out from the door and you could almost reach out and grab it. 
There is many pictures like this that try and convince us that the bjects that we are seeing are real, even though they're reconstructed by technology. In this case, of course, it's paint in a canvas, but we can see that there is a long history of these things, these types of illusion. 
So what I'm showing now is a picture from a panorama, 
which was installed in Leicester Square. 
Now, today Leicester Square is sort of a tourist central in London. 
There are many large theaters around it, it's the center of theater land and 
cinemas and so. 
But this panorama, this is shown in an etching from 1801, 
with this sort of state of the art of immersive entertainment at the time. 
And what you can see is a four story building, and 
constructed inside this building is a painting, and 
it's a painting that shows a landscape with a sea and boats on it. 
And you can see in the center of the painting that people are climbing up some 
stairs to look out at this immersive picture. 
And again, this is a type of phenomena which you can 
understand sort of inspired early developers of virtual reality technology. 
Again, it's his virtual reality, 
he's trying to create the impression of a place which is somewhere else. 
So throughout this period of 1800s, 1900s, 
you can see many examples, in museums across the world. 
Of items which we can now refer to, where we now can recognize this sort 
of precursor of the technology where we now take for granted as virtual reality. 
So for example, this is a picture of something called a stereograph. 
The stereographs are invented not long after the invention of photography. 
Where the photographer takes two pictures from slightly different points of view. 
And therefore when you put them with a stereoscope together you can confuse 
an image. 
You can actually do this on the screen if you're so inclined, 
if you cross your eyes over you can form this into a stereo image. 
And this picture from the Library of Congress is showing a woman actually 
looking at a stereograph, stereoscope, so showing the technology of the time. 
And to be completely frank, head mount displays aren't really technically much 
more sophisticated than this. 
You have a head mount display has two screens showing two images, and 
whereas before this was done with prints. 
So you would print a photograph and show it on the little device. 
Now we are using screens. 
When we're moving towards the 20th century what we are seeing then is 
an increasingly set of dynamic illusions. 
And this was really inspired by the need to train people, 
in particular training people like pilots. 
So the first simulators for training pilots came in the First World War, 
so there was a need to train a lot of people very quickly. 
And this picture shows a very common training system 
called the Link Trainer, from the Second World War. 
The idea here is that it simulates some of the controls of an airplane so 
that you don't have to have your first flight in a single seat airplane. 
Now, these were almost essential during the war effort, 
but now one of the foundations of the technology we now use. 
The flight simulators have been a very big part of virtual reality since 
the Second World War, 
with many companies specializing in flight simulators for example. 
Companies like Evans & Sutherland, then develop these systems to be digital. 
So no history of the analog virtual reality would be complete without 
mentioning Morton Heilig's Sensorama simulator. 
So this is really the last system of this part of the lecture. 
So in the Sensorama simulator you see a combination of effects. 
You see a booth that you sit in and 
you put your head up against a display and it shows you stereo wide angle films. 
You also get 3D sound, you also, unlike many systems, you get audio. 
So you get wind effects, you get aroma effects, and 
the device actually shakes a little bit. 
And this is really the culmination of the analog technologies that are available 
to filmmakers and creative individuals. 
So that's it for this video about analog virtual reality technologies. 
In the next video, 
we'll start with the history of digital virtual reality technologies. 
[MUSIC] 
Virtual reality, then, to get more flexible than this, 
you can't film, you can't take analogue media, and 
make it much more flexible than watching a static story. 
So, it's when we get to the digital age that we start to see 
that we can get what we now consider to be virtual reality. 
The key parts being that the person can move around, 
they can choose their own point of view in the film, and 
they can experience audio from a first person point of view. 
So a seminal system of this 
start of this digital age is Ivan Sutherland's Sword of Damocles System. 
So this was built in 1968 and is 
really what most people considered to be the first digital, virtual reality system. 
It was quite a large contraption. 
It's a head mounted display, 
which is suspended from the ceiling from a mechanical gantry. 
But it had all of the facilities that we expect of virtual reality, 
in that the head mounted display tracks what the person is doing with their head. 
So they move around, it changes the graphics. 
Those graphics are rendered from a first person point of view. 
So as they move around and look, the graphics would change in the same manner. 
So this being so early was quite crude. 
Of course it was y frame graphics and 
very low fidelity, but it's got some of the essential features and 
we'll see throughout the head mounts displays. 
So if we jump forward 10 years, or 20 years even, 
we get to a system that is now starting to be built in industry. 
So this is a system called the VIEW workstation from NASA. 
This was built in the 80s. 
And this picture's from the 1989. 
And what you can see here is sort of the prototype of what we now consider to 
be a virtual reality system. 
No large mechanical assembly, what you can see is something that sits on the head. 
It's got a large box at the front with screens and 
the person can move around freely. 
You can also see that the user is wearing headphones and 
also that they have gloves on their hands so that this system 
can track their finger movements, it can also track where they're pointing. 
So this system was used by NASA for 
various projects, including training astronauts. 
And then, this was sort of the start of the industry in the 1990s. 
Some of this technology was then taken by a company called VPL, and 
which was in part founded by who's a name you'll come 
up against in many histories of virtual realities, 
being the most visible of the pioneers of the early 90s. 
So what I'll show you now is where I get started in the field 
when I was a Ph.D student. 
So, what you see in this, 
this video is really what the state of the art was at the time. 
This is a virtual reality system based on a head mounted display called the virtual 
research flight helmet and driven by a system called the division provision. 
Now, I have the head mounted display here, it's not functional anymore. 
But it's got all the bits that we might expect to see in a head mounted display. 
Now importantly, it's got on here, a tracking devices. 
This is a tracker. 
So this tracks where this whole head mounted display is. 
It also, inside, has two screens. 
And this has been taken apart for various experiments. 
And actually pull the screens out and these little television screens, 
portable television screens from the late 1980s, early 90s. 
So, together with a fast computer you can use the headmount display 
tracking information to generate a picture on here that the person can see. 
Now, there's one important bit which I haven't shown you because I've taken it 
out to show separately. 
And that's this. 
This is the leap optics. 
This is the optical system that goes inside the head mount display. 
And this, if you hold up to your face, 
generates a very wide field of view of the screen. 
So the screens are quite small but once you put this in, 
you're seeing about a 100 degrees field of view. 
So, it has a great sense of immersion inside the virtual world. 
But as you can see in the video, that world is quite crude. 
So it's not very visually realistic, it's only got a few hundred polygons in it. 
But even then, we were starting to see some interesting phenomena. 
So this is a part of a demonstration we've had in 1993. 
And this shows somebody standing on a plank, looking over an edge down into. 
Now this phenomena, this experience for the user is quite dramatic. 
Though when the person looks at the image, and remember they've got a head-mounted 
display, and they're looking down, they're showing signs of fear. 
And it's very crude graphics, as you can see. 
It's only got a few hundred polygons, there's just a box with a plank. 
There's a plane, looks about 20 feet below you, where you could fall on. 
But the person is visibly shocked. 
And their fear of heights was something we noticed very early on, and 
that virtual reality, even when it was quite so crude, was able to elicit. 
So those systems were then, that one inspired our research and similar 
phenomenon inspired a lot of people over the past 20 years in virtual reality. 
And these days you can find that plank illusions or virtual drop illusions can be 
found in almost all consumer virtual reality systems. 
So it won't be too hard for you to find one to try yourselves. 
So in the 1990s there was this big interest in virtual reality and 
you could find it in quite a few places. 
So here I'm showing a picture from a commercial system, which you can find in 
many arcades or tourist attractions, called the virtuality system. 
And this was a fairly bulky head-mount display, but it had all the same elements. 
It had head tracking. 
It also had trackers for the hands so that you could point at things in the world. 
And you could play various games in the system. 
And these, although they're expensive to store and run, 
were quite popular for about ten years. 
But the big problem was really that you needed 
a lot of compute power to drive these systems. 
Computers at the time of course, home computers, were not very powerful at all. 
It was actually quite rare to have a 3D graphics accelerator. 
So our systems were expensive and the systems in arcades were also expensive. 
But over the next ten years, systems did get cheaper and 
people did try to make consumer electronics. 
So this is a VFX1 Forte head mounting display. 
And it's one of an example of many examples of people trying to commercialize 
virtual reality systems for the consumer market. 
It didn't take off at the time, and to be honest, the main reason for 
that is just the quality of the graphics. 
And also a phenomenon that it's quite disrupting to the user which is lag. 
So unfortunately when the person moves their head around, 
the images would take a little bit time to catch up. 
And this with the two computers at that time would be quite long. 
So 100, 150 milliseconds wasn't too uncommon. 
But having said that, what you can see is that there was a lot of interesting 
research done on virtual reality, and 
we can see in this video again from our laboratory. 
That somebody is going into the head mounted display, 
they're standing in a room which is actually a copy of the lab. 
So the 3D model is of the lab. 
They're wearing a different head mounted display, 
this time it's a bit more sophisticated. 
This is Virtual Research VR 1280. 
This one still works. 
It's actually still the highest resolution head mounted display 
in the lab until about two years ago. 
And it gives a more convincing sense of presence. 
The computers have got better. 
You'll see in the video, if you look carefully, you actually see a little 3D 
model of the computer that we use, which was silicon graphics onyx system. 
And what you see in the video is somebody using a virtual body, 
and reaching out and touching. 
And this experiment was one of several that we ran which were to show that 
the virtual body has a big impact on how the person interacts in the virtual world. 
Okay, so we've come to describe the early virtual reality systems, 
so,now let's talk a bit about where it went. 
So the public perception of virtual reality is that it went away, 
in the late 90s and early 2000s. 
But in actuality it became more of a professional system. 
You saw Labs investing in equipment that could produce virtual reality but 
at a higher cost because it was so interesting to study. 
And an important system which many labs built is 
a variant of a system called the CAVE. 
So the CAVE is a recursive acronym, it stands for 
cave automatic virtual environment. 
And the first one was invented by Carolina Cruz-Neira, Daniel Sandin, and 
Thomas DeFanti of the University of Illinois. 
And this has a very different structure to a head mount display. 
In a head mount display you wear the images on your head, but 
in a CAVE-like system the images are on the walls around you, so that you, you see 
the projection and that the computer has to update the images on the walls. 
You still need a head tracker. 
You will need to wear some small glass, 
because you want to have a stereo image inside for the user. 
But the big advantage of these systems is that the perception of latency or 
lag when you move your head is very low. 
So actually in our system which we're showing here which is 
the CAVE-like system that we have at University College London. 
We almost never found anybody got ill or 
suffered negative symptoms when using this system. 
So this image shows a typical cave that's got three walls and a floor. 
And each wall can be dedicated to a separate computer, so 
you've got that idea of using multiple computers now to get the speed and 
the quality of the graphics that you want. 
And these became reasonably 
common in laboratories that are interested in virtual reality. 
They also became quite common in certain engineering disciplines. 
So what we've got here is a picture of 
a system that was built at Jaguar Land Rover in the United Kingdom. 
And they used the CAVE-like systems to investigate aspects of their cars. 
So, for example, how the user might interact with the car. 
Not just using the steering wheel, but, for example, 
fitting things, in and out, of the boot space in the car. 
And that gave them big advantage compared to other means of doing that types 
of task. 
Because these are engineering tasks that are very three-dimensional. 
You need to have a very good idea about where the objects are, and 
how to manipulate them. 
So CAVE systems, and head mounted displays of course, will give you a good sense of 
the proximity and the space of the objects that you're looking at. 
Of course if you had the budget, you could buy a very high end head mounted display. 
So several companies were making head-mounted displays, 
servicing industry, academia that wanted to get those high quality systems. 
So this picture is of an NVIS 111 head-mounted display. 
Which is an admittedly expensive but very high quality 
head-mounted display that's about five to ten years old. 
What I wanted to convey there is that virtual reality continued to evolve, 
it continued to get better equipment and 
the science of understanding virtual reality progressed quite dramatically. 
But it's really with the confluence of 3D image generators, 
graphics cards that were driven by consumer technology, that we really start 
to see a vast acceleration in the quality of virtual reality. 
And there's really a point to note, which is that in the early 
2010s, so 2011, 2012, several groups were now sort of looking at 
the possibilities of using consumer electronics for virtual reality. 
So I'd like to mention just a couple of them. 
One is the field of view to go system, or 
FOV to go system from the University of Southern California. 
And what they built was a system which you can make yourself, you can still make, 
the plans are freely available. 
That you could put a phone or an iPad in and 
you could then have a virtual reality system that you could hold to your face. 
And later on of course we come across systems like [INAUDIBLE] cardboard which 
take the same principle and apply it to a much cheaper way of fabrication. 
But the key thing of that is really of that system, the smartphones, 
iPhone 4S in particular Had reached the level of quality of real time 
computer graphics that they could be considered to be suitable for 
putting inside head-mounted displays. 
This is another system, 
this actually is a system that we built at University College London. 
It actually uses a very old head mounted display, or 
relatively old head mounted display called a Sony Glasstron. 
This is from the late 1990s, but it's driven now off a smartphone. 
So it's driven off an iPhone 4S. 
And that with generating a solid 60 frames per second, 
so you could turn your head and you could see the same 
virtual reality that you might see on one of these high end systems that we had. 
That cost a lot more. 
So now, you're looking at their components, 
obviously this was an expensive head mounted display. 
But you see, it's only got a couple of screens and 
the images are generated by smartphone. 
So there isn't much, more that we need, more specialized equipment. 
So then, of course, we get to perhaps the most 
disruptive system is that in 2012, 2013, 
we start to see the emergence of truly consumer systems. 
So with the system, 
the Oculus Rift developer kit 1, or DK1 was launched in 2013. 
And now we're here, so now we have the very cheap, 
high quality, consumer head mounted display. 
At the same time, we've got the power in our desktop computers that really means 
that we can have effective high quality virtual reality in everybody's home. 
And that's why we're here, that's the point of 
this course is that to learn all about well how this 
technology is going to be used in the next few years. 
[MUSIC] 
```

## History of VR

Virtual reality has beginnings that preceded the time that the concept was coined and formalised. In this detailed history of virtual reality we look at how technology has evolved and how key pioneers have paved the path for virtual reality as we know it today.

### Early Attempts at Virtual Reality
#### Panaromic paintings

If we focus more strictly on the scope of virtual reality as a means of creating the illusion that we are present somewhere we are not, then the earliest attempt at virtual reality is surely the 360-degree murals (or panoramic paintings) from the nineteenth century. These paintings were intended to fill the viewer’s entire field of vision, making them feel present at some historical event or scene.

#### 1838 – Stereoscopic photos & viewers

In 1838 Charles Wheatstone’s research demonstrated that the brain processes the different two-dimensional images from each eye into a single object of three dimensions. Viewing two side by side stereoscopic images or photos through a stereoscope gave the user a sense of depth and immersion. The later development of the popular View-Master stereoscope (patented 1939), was used for “virtual tourism”. The design principles of the Stereoscope is used today for the popular Google Cardboard and low budget VR head mounted displays for mobile phones.

- 1838 : The stereoscope (Charles Wheatstone)
- 1849 : The lenticular stereoscope (David Brewster)
- 1939 : The View-Master (William Gruber)
    
Over time mankind has been slowly but surely creating ever richer ways to stimulate our senses. Things really began to take off in the 20th century, with advent of electronics and computer technology.

#### 1929 – Link Trainer The First Flight Simulator

In 1929 Edward Link created the “Link trainer” (patented 1931) probably the first example of a commercial flight simulator, which was entirely electromechanical. It was controlled by motors that linked to the rudder and steering column to modify the pitch and roll. A small motor-driven device mimicked turbulence and disturbances. Such was the need for safer ways to train pilots that the US military bought six of these devices for $3500. In 2015 money this was just shy of $50 000. During World War II over 10,000 “blue box” Link Trainers were used by over 500,000 pilots for initial training and improving their skills.

Left: Edward Link, Right: The Link Trainer

#### 1930s – Science fiction story predicted VR

In the 1930s a story by science fiction writer Stanley G. Weinbaum (Pygmalion’s Spectacles) contains the idea of a pair of goggles that let the wearer experience a fictional world through holographics, smell, taste and touch. In hindsight the experience Weinbaum describes for those wearing the goggles are uncannily like the modern and emerging experience of virtual reality, making him a true visionary of the field.
 Image source: sffaudio.com

#### 1950s – Morton Heilig’s Sensorama
In the mid 1950s cinematographer Morton Heilig developed the Sensorama (patented 1962) which was an arcade-style theatre cabinet that would stimulate all the senses, not just sight and sound. It featured stereo speakers, a stereoscopic 3D display, fans, smell generators and a vibrating chair. The Sensorama was intended to fully immerse the individual in the film. He also created six short films for his invention all of which he shot, produced and edited himself. The Sensorama films were titled, Motorcycle, Belly Dancer, Dune Buggy, helicopter, A date with Sabina and I’m a coca cola bottle!
   
Image source: mortonheilig.com

#### 1960 – The first VR Head Mounted Display

Morton Heilig’s next invention was the Telesphere Mask (patented 1960) and was the first example of a head-mounted display (HMD), albeit for the non-interactive film medium without any motion tracking. The headset provided stereoscopic 3D and wide vision with stereo sound.
#### 1961 Headsight – First motion tracking HMD
In 1961, two Philco Corporation engineers (Comeau & Bryan) developed the first precursor to the HMD as we know it today – the Headsight. It incorporated a video screen for each eye and a magnetic motion tracking system, which was linked to a closed circuit camera. The Headsight was not actually developed for virtual reality applications (the term didn’t exist then), but to allow for immersive remote viewing of dangerous situations by the military. Head movements would move a remote camera, allowing the user to naturally look around the environment. Headsight was the first step in the evolution of the VR head mounted display but it lacked the integration of computer and image generation.
#### 1965 – The Ultimate display by Ivan Sutherland
Ivan Sutherland described the “Ultimate Display” concept that could simulate reality to the point where one could not tell the difference from actual reality. His concept included:
- A virtual world viewed through a HMD and appeared realistic through augmented 3D sound and tactile feedback.
- Computer hardware to create the virtual word and maintain it in real time.
- The ability users to interact with objects in the virtual world in a realistic way

> The ultimate display would, of course, be a room within which the computer can control the existence of matter. A chair displayed in such a room would be good enough to sit in. Handcuffs displayed in such a room would be confining, and a bullet displayed in such a room would be fatal. With appropriate programming such a display could literally be the Wonderland into which Alice walked. – Ivan Sutherland

This paper would become a core blueprint for the concepts that encompass virtual reality today.

#### 1968 – Sword of Damocles
In 1968 Ivan Sutherland and his student Bob Sproull created the first VR / AR head mounted display (Sword of Damocles) that was connected to a computer and not a camera. It was a large and scary looking contraption that was too heavy for any user to comfortably wear and was suspended from the ceiling (hence its name). The user would also need to be strapped into the device. The computer generated graphics were very primitive wireframe rooms and objects.
  
#### 1969 – Artificial Reality
In 1969 Myron Kruegere a virtual reality computer artist developed a series of experiences which he termed “artificial reality” in which he developed computer-generated environments that responded to the people in it. The projects named GLOWFLOW, METAPLAY, and PSYCHIC SPACE were progressions in his research which ultimately let to the development of VIDEOPLACE technology. This technology enabled people to communicate with each other in a responsive computer generated environment despite being miles apart.
#### 1987 – Virtual reality the name was born
Even after all of this development in virtual reality, there still wasn’t an all-encompassing term to describe the field. This all changed in 1987 when Jaron Lanier, founder of the visual programming lab (VPL), coined (or according to some popularised) the term “virtual reality”. The research area now had a name. Through his company VPL research Jaron developed a range of virtual reality gear including the Dataglove (along with Tom Zimmerman) and the EyePhone head mounted display. They were the first company to sell Virtual Reality goggles (EyePhone 1 $9400; EyePhone HRX $49,000) and gloves ($9000). A major development in the area of virtual reality haptics.
  
 
#### 1991 – Virtuality Group Arcade Machines
We began to see virtual reality devices to which the public had access, although household ownership of cutting edge virtual reality was still far out of reach. The Virtuality Group launched a range of arcade games and machines. Players would wear a set of VR goggles and play on gaming machines with realtime (less than 50ms latency) immersive stereoscopic 3D visuals. Some units were also networked together for a multi-player gaming experience.
#### 1992 – The Lawnmower Man
The Lawnmower Man movie introduced the concept of virtual reality to a wider audience. It was in part based on the founder of Virtual Reality Jaron Lanier and his early laboratory days. Jaron was played by Pierce Brosnan, a scientist who used virtual reality therapy on a mentally disabled patient. Real virtual reality equipment from VPL research labs was used in the film and the director Brett Leonard, admited to drawing inspiration from companies like VPL.
#### 1993 – SEGA announce new VR glasses
Sega announced the Sega VR headset for the Sega Genesis console in 1993 at the Consumer Electronics Show in 1993. The wrap-around protoype glasses had head tracking, stereo sound and LCD screens in the visor. Sega fully intended to release the product at a price point of about $200 at the time, or about $322 in 2015 money. However, technical development difficulties meant that the device would forever remain in the prototype phase despite having developed 4 games for this product. This was a huge flop for Sega.
 
#### 1995 – Nintendo Virtual Boy
The Nintendo Virtual Boy (originally known as VR-32) was a 3D gaming console that was hyped to be the first ever portable console that could display true 3D graphics. It was first released in Japan and North America at a price of $180 but it was a commercial failure despite price drops. The reported reasons for this failure were a lack of colour in graphics (games were in red and black), there was a lack of software support and it was difficult to use the console in a comfortable position. The following year they discontinued its production and sale.
  
#### 1999 – The Matrix
In 1999 the Wachowski siblings’ film The Matrix hits theatres. The film features characters that are living in a fully simulated world, with many completely unaware that they do not live in the real world. Although some previous films had dabbled in depicting virtual reality, such as Tron in 1982 and Lawnmower Man in 1992, The Matrix has a major cultural impact and brought the topic of simulated reality into the mainstream.
#### Virtual reality in the 21st century
The first fifteen years of the 21st century has seen major, rapid advancement in the development of virtual reality. Computer technology, especially small and powerful mobile technologies, have exploded while prices are constantly driven down. The rise of smartphones with high-density displays and 3D graphics capabilities has enabled a generation of lightweight and practical virtual reality devices. The video game industry has continued to drive the development of consumer virtual reality unabated. Depth sensing cameras sensor suites, motion controllers and natural human interfaces are already a part of daily human computing tasks.

Recently companies like Google have released interim virtual reality products such as the Google Cardboard, a DIY headset that uses a smartphone to drive it. Companies like Samsung have taken this concept further with products such as the Galaxy Gear, which is mass produced and contains “smart” features such as gesture control.

Developer versions of final consumer products have also been available for a few years, so there has been a steady stream of software projects creating content for the immanent market entrance of modern virtual reality.

It seems clear that 2016 will be a key year in the virtual reality industry. Multiple consumer devices that seem to finally answer the unfulfilled  promises made by virtual reality in the 1990s will come to market at that time. These include the pioneering Oculus Rift, which was purchased by social media giant Facebook in 2014 for the staggering sum of $2BN. An incredible vote of confidence in where the industry is set to go. When the Oculus Rift releases in 2016 it will be competing with products from Valve corporation and HTC, Microsoft as well as Sony Computer Entertainment. These heavyweights are sure to be followed by many other enterprises, should the market take off as expected.

##### References
https://humansystems.arc.nasa.gov/groups/acd/projects/hmd_dev.php

Components of VR:
- VR Display, for instance, HMDs
- VR Content, which refers to the images that are on display that you can sometimes interact with.
- VR Interaction, which is usually supported by VR Controllers

## VR Technical Framework

In the next few videos, we'll talk about applications in virtual reality. So far we've learned about VR hardware. 
We've learned that a typical high-end VR hardware would come with two parts. 

The first part is a VR display, which provides surrounding 3D stereo vision, and allows the user dynamic control of their view point, the precision and rotation tracking. 

The second part is a pair of VR controllers which support 
3D user interaction with our hands. So just like how we use our hands in real life, in virtual reality, we can use our hands to select and manipulate virtual objects, and to gesture, and interact socially. 
Another way to look at VR and how it differs from other media is that it consists of three parts. The VR display, for instance, HMDs.  VR interaction, which is usually supported by the VR controllers. 

And VR content, which refers to the images that are on display that you can sometimes interact with. 
Some people would argue that only real-time 3D graphics and animation count as VR content. 
But nowadays the term is very often used to include 360 degree video or images. 
We will discuss the differences between these two types of VR content later. 
Now I'd like to explain why it could be useful to divide VR into these three components, and how I use this as a framework to think about VR applications.  Personally, I find this a useful framework for understanding VR applications. 

For instance, if I want to design a VR ping pong application, I start by thinking about how we play ping pong in real life, and how everything carries over to VR. 

I have to think that when you play ping pong or table tennis, it's important that you're able to move your body around. So to make it more natural, we will meet a VR display with position tracking. 

In this case, mobile VR would be less suitable. 

Secondly, you will need to hold your ping pong bat. 
Its position and orientation will have to be both tracked. 
And ideally when you hit the ball, you should be able to have some simple haptic feedback. 

Finally, for VR content we'll need both 3D graphics and animation. 
So we'll need to program a simple physical simulation to animate a ball 
using Newton's laws of motion. 
But the graphics and animation do not need to be very sophisticated to be effective, so there won't be any frame rate or latency concerns. 

So it's clear that hardware is available on the market to support this. 
We will need high-end VR hardware supported by desktops. 
There is a slight issue here, as those devices are currently not wireless. 

This is fine with a game like ping pong because you never really need to 
be particularly far from the table, so all you need is a relatively small space. 
But the same setup wouldn't work for tennis in which you have to move around a much bigger space. 
So ping pong will be a good VR application, as it is well supported by the current VR hardware. 
Let's have a look at another example. If you would like to design a VR shopping application which allows users to buy clothes, then you will realize that you might have some problems. 

Again, let's think about what you would do in real life. 
In real life when I shop for 
clothes, I would definitely want to try them out to see how they look on me. 
So VR display is not a problem here, as it can even be mobile VR. 
However, I would also like to be able to really feel the texture of the material. 
When it comes to VR interaction, the ability to actually 
feel the textures in VR would go beyond the current VR hardware. 
So this might not be a good idea. 
Another problem could be VR content. 
Ideally, you would have a big database of 3D models of clothes you are selling. 
But you would also need a physical model of the body of your customer. 
You could then use physical simulation to show 
how the clothes might fit on the body of your customer. 
The problem here is that 3D scanning and 
physical simulation of soft material are both very difficult challenges. 
You might say that you'd like to design an application where customers can just look 
at the clothes in a VR display without being able to touch them or try them on. 
In that case, my question is do you still need to be in VR? 
Why don't you just use a desktop 2D application instead? 
After all, VR is still more difficult to set up, and 
the resolution is still fairly low compared to an average desktop display. 
So with the current technology, shopping for 
clothes in VR might not add much to the online shopping applications, 
unless you have some clever ways to solve the problems mentioned previously. 
[MUSIC] 

#### A Brief history of VR
So now, can you maybe tell us a little bit about 
the history of VR and what is really the magic behind it. 
Yes, actually people think that 
virtual reality is something that just started two or three years ago, 
but it goes back a long way. 
The first systems were developed and the concepts, 
the fundamental concepts that we still use today were developed in the 1960s by 
Ivan Sutherland who invented a machine code that he called The Sword of Damocles. 
His idea was to lead towards the ultimate display. 
I'll come back to that in a few minutes. 

Twenty years later in the 1980s, NASA Ames were also building virtual reality systems called The View system. 
In the late 1980s, Jaron Lanier who is the man who invented the term virtual reality, he worked on the system called Reality Built For Two, 
and probably he's one of the people who most popularized the idea in the late 1980s and early 1990s. The hardware concepts that we have today about virtual realities really go back all that way to the 1960s. 
Basically what the hardware involves is some way of replacing our sensory operators by computer generated sensory operators. 

In particular, let's think about vision, the idea of the Sword of Damocles, the original head-mounted display developed by Ivan Sutherland, was that you had two eyepieces which were essentially think of them as computer displays that you saw through small lenses, and there was a big contraption that was hanging off the ceiling which did mechanical tracking of your head movements. 

So these eyepieces had computer displays on them, very small computer displays that you saw through lenses. But as you moved your head around, 
so the scene you saw was updated based on the mechanical tracking. 
So if I turned my head over here, what you saw inside this Sword of Damocles head-mounted display would similarly update. 
You'd see a different part of the scene just like in real life as 
I turn my head around so I see different parts of the real thing. 

Now, why two eyepieces? One for the left eye one for the right eye, 
and each one had projected onto it or each one rather displayed the vision appropriate for that eye. So the left eye saw only a left eye view, the right eye only a right eye view, and the brain fuses those together just like in real life into one overall three-dimensional stereo image. 

So not only does what you see change according to your head movements, 
but what you see is also in stereo. 
So it gives you a very strong illusion that you're in 
the place which is being displayed by the computer screens. 
And let's remember that in the 1960s the kind of 
computer graphics displays they had then were much simpler than what we have now. 
Now we have full color displays with solid colors and it looks very realistic. 
All they had in the 1960s were green lines. 
So if I was in a room, 
a virtual room depicted in these 1960 displays, 
it would just be a set of green lines 
mapping out the edges of the room and the objects in it and so on. 
Yet nevertheless even at that time, 
even with that kind of display, 
Ivan Sutherland reported that people had this strong sense of what we now call presence, 
the sense of being in the world described by the computer displays. 
So the fundamental, you asked about the magic, 
the fundamental magic is that 
the computer displays because they're tied to your sensory operators very closely, 
you move your head and the image changes. 
You see in stereo, 
they give you the illusion that you're in the place depicted by 
the virtual reality rather than in the real world where of course you really are. 
So this is part of the magic, 
this wow factor that Sylvia mentioned earlier. 

## Levels of Immersion in VR Systems

```
So Mel, can you explain what is the definition of immersion, 
which is something often used to describe 
VR experiences and also in particular, nowadays, 
we have all these fascinating VR displays that enables 
us to really see things in 3D with stereo vision? 
But how does other aspect of VR, 
which enable us to interact with it, 
and how does that link back to the concept of immersion? 
Okay. So I'm going to talk about 
an ideal system rather than the systems that we have today. 
So in an ideal system, 
it would display in all sensory systems. 
So what I mean by that, of course, 
we are most familiar with vision, but, 
of course, there's also sound which is pretty feasible. 
But even if you think about sound, 
there's many different ways that sound itself can be portrayed. 
So it could just be sound not coming from any particular direction. 
It could be specialized sound, 
so that when in virtual reality, 
an event is happening over there, 
I hear it from over there. 
Or it could represent how sound is reflecting through an environment a particular room. 
So it's properly modeled sound. 
So just as with vision, 
there's many different levels of vision that you could have from very simple 
to realistic simulation of how light flows in an environment. 
So the same is true of sound, 
but all of these things, 
more or less, is pretty well today. 
So there's also haptics. 
Haptics is two aspects, 
the sense of touch when you touch something, 
you feel it and different surfaces have different feelings. 
And the other aspect of haptics is force feedback. 
If something touches you or pushes you, you feel the force. 
So a true ultimate virtual reality system would support both of those. 
And today, it does to some extent. 
So, for example, there are haptic devices where you 
can feel particular kinds of touch feedback, 
and there are haptic devices, 
quite complicated ones, where you can feel forced feedback. 
But, unlike vision, so one visual display device can represent any kind of visual input. 
For haptics, it's not like that. 
For each kind of haptics, 
there's a special device. 
So you can have a really good device that gives you 
the feeling of pushing a needle through flesh, for example, 
if you're using it for training in surgery, 
or you can have a haptic device where you're touching materials and it feels realistic. 
But there's no generalized haptic device in the sense of, 
in real life, I can be walking along and 
my elbow happens to brush against the wall and I feel it. 
There's no generalized haptic device here in virtual reality, 
which makes this possible, 
and there's certainly no force feedback device. 
For example, if a virtual character in virtual reality pushes my shoulder, 
I'm typically never going to feel it because there's no device. 
There's certainly no general device that does that. 
So haptics is an area of which requires a lot of development to get towards, 
let's say, what was Ivan Sutherland's dream of the ultimate display. 
And another one is smell. 
So, of course, there again are 
particular systems that can deliver smell in virtual reality, 
but there is again no generalized smell system. 
One of the problems with smell is that once it's in a place, 
it doesn't go away very easily. 
So you can make a smell, 
let's suppose you're in the virtual reality, 
you're going into a place where there's been a fire, 
and you smell the fire. 
So something has to come in real life that makes you smell the fire. 
But then when you go out of that place, 
that smell of fire is still going to linger because it's going to be in the real world. 
So if we go through the various sensory operator's vision and sound, 
they're pretty well-cared for in today's systems. 
But, of course, there's lots of room for improvement even in those. 
Haptics is very, very good particular haptic devices but no generalized haptics. 
The same is also true of smell. 
Can I just add something about smell? 
Because that just reminded me, 
I visited a lab in Switzerland where, basically, 
in order to simulate a smell and to solve that problem you've 
mentioned to get the smell actually out of the way after you 
change to a different environment is that they put 
a little pipe into my nose which pumps oxygen constantly. 
But then when I get close to a particular object in VR, 
I can just smell that object, 
but when I move away, obviously, 
they start pumping oxygen instead. 
So that's probably one way to do it. 
So it's really fascinating to think about all this potentials of VR, 
different VR systems we could develop in the future. 
And so my question here is, 
is there a way to actually measure immersion to kind 
of have a way to compare different VR systems? 
Is one more immersive than the other? 
It's very important to understand what we mean by immersion in 
virtual reality because it's a term overused. 
So we might say, "Oh, 
I felt very immersed," or "I felt this was immersive," and so on. 
But what do we really mean by immersion? 
To me, immersion is the description of a system. 
It's a technical description of what a system can deliver. 
So for example, if we take two head-mounted displays, 
one that tracks in four degrees of freedom, 
six degrees of freedom, 
which means I can turn my head in any direction and I can translate my head like this, 
and I can turn in any direction, 
and always, the feedback will be correct. 
The visual feedback and the sound feedback will be correct for 
those movements because my head is tracked in all six degrees of freedom. 
And then compare that with another head-mounted display, 
which only tracks in terms of rotation. 
So if I turn my head, it's okay, 
but if I translate, nothing happens. 
So these are two different types of immersion, and I would say, 
the way I think about it is the first one that tracks in 
six degrees of freedom is more immersive. 
I mean, immersive in this technical sense because you can use 
the first one to simulate the second because the second is a subset of the first. 
The second one, we can only track rotations but not translations. 
It's a subset of the one where you can track in all six degrees of freedom. 
And this is actually really important because it gives you 
qualitatively different experiences and different information. 
Because if I go like this and nothing happens, 
well actually, two things will happen. 
One is I'm likely to get quite sick because I'm moving my head but 
the world is not updating or my visual display is not updating accordingly. 
And second, it means, well, 
I can't look close to an object. 
I can't look further away an object. 
I can't look behind an object by moving my head. 
And this is something very real. 
For example, in today's head-mounted displays, 
typically the ones based on phones where you slot your smartphone into a casing, 
they only have the rotational kind of 
head-tracking because they're based on the inertial system of the phone. 
Whereas a head-mounted display, 
which has a head-mounted display in itself, 
not just a phone, typically, 
they have the full six degrees of freedom tracking. 
So if we generalize this idea, 
I would say one system is more immersive than 
another if the first can be used to simulate the second. 
Should I give another example? 
Actually, because we spent lots of time discussing in 
this course the difference between CAVE and HMD, 
so which one of these two systems you think is more immersive? 
Remember, I'm talking about a technical definition. 
I'm talking about specification of the system, 
the hardware and software. 
At this, moment I'm not talking about the effect of 
those on you though I gave that as an example that they do have different effects. 
But I'm only talking about the technical specification. 
So a head-mounted display with full six degrees 
of freedom tracking is more immersive than 
the CAVE because I could use a head-mounted display to 
simulate the whole process of going in a CAVE and being in a CAVE. 
But I can't use a CAVE to simulate 
the process of picking up a head-mounted display and putting it on. 
That's just not possible. 
Or if we take another example, 
for many years, people talked about desktop virtual reality. 
So desktop virtual reality was that you'd sit in front of 
a monitor and maybe with stereo vision, 
you wear glasses and so on and you see stereo on the screen. 
Some people call this virtual reality or desktop virtual reality. 
Virtual reality through a full head-tracked head-mounted display is more immersive than 
desktop virtual reality because I can use 
the full head-mounted display system to simulate a desktop system. 
So this is what I mean that there's various levels 
of immersion that when you have system A and System B, 
then you can use A to simulate B, 
then A is more immersive than B. 
The last point on this, this doesn't apply to all systems, 
so I could have two systems X and Y, 
where X can't be used to simulate Y, 
and Y can't be used to simulate X. 
This immersion is not like a full ordering of all possible systems, 
is what's called in mathematics, a partial order. 
So one example you can think of is probably when you are in 
the CAVE comparing to when you're in a sort of IMAX cinema, 
where they come very sort of simulate each other. 
Yeah, they're different. 
Yeah. Because in the cave, for instance, 
when you turn back, normally, you don't have the back wall. 
So it doesn't actually 100% simulate 
experience you can have in IMAX and definitely not the other way. 
Yeah. You couldn't use either of those to simulate the other. 
Yeah. And I'm talking about simulation in principle. 
I mean as an ideal, 
not like an actual hardware and so on. 
```

## Sensorimotor Contingency (SC)
```
[MUSIC] 
So Mel, I remember at some point, doing my PhD, 
you mentioned the concept of sensory motor contingency, and that's really, 
for me, the point that a lot of the things in VR started to make sense. 
So maybe we should talk about the definition of this and 
how it actually works in real life. 
>> Yes, so sensory motor contingencies is part of the theory of 
active vision that describes how we use our body's to perceive. 
So basically we have a set of implicit rules that we use to perceive the world. 
Rules that we got by implicit, I mean, there are rules that we don't have to 
think about, we just know them, but on the other hand they are rules. 
So I know, to look behind you, I go like this. 
I didn't have to think, how am I going to look behind her, I just do it. 
>> And I automatic duck my body. 
>> [LAUGH] Yeah, so there are rules where we think of vision 
essentially as we often think of it as something passive. 
We take vision as an example, that the light just comes into our eyes and we see, 
but no, we're always acting, we're always moving. 
So we turn our head, we move, we bend down. 
In terms of tactile feeling, we reach out, we touch things. 
Very active using my body, I feel my muscles changing as I 
reach our my arm, it gives me a sense of distance as well. 
So overhearing to hear something better, 
you might turn your ear towards it, and so on. 
So by sensory motor contingencies we mean that set of implicit rules, 
whereby we use our body to perceive the world across all the different senses. 
[MUSIC] 

[MUSIC] 
So before we talked about the concept of immersion as being 
the affordances that the system gives you, but very important in 
that is what affordances does the system give your for perception? 
So for example, if I'm wearing a head mounted display that has no head tracking, 
I can move my head as much as I like and 
I won't get sensory motor contingencies which are caused by moving my head. 
The image I see will always just move with me, nothing will change. 
But if I have head tracking with let's say 
46 degrees of freedom head tracking, as I turn around and as I move my head, so 
the visual system, the visual input I get will update accordingly. 
Which means that I have sensory motor contingencies that are more or 
less the same like real life. 
But sensory motor contingencies has another aspect. 
It's not just simply the interaction, 
the input, it's also how we input it. 
So part of sensory motor contingencies is that, as I said, 
if I want to see close up to this object, I just move my head closer to it and 
I see that object closer. 
But how is VR involved in this? 
VR is involved because in VR if I do the same, not exactly the same 
thing will happen, because eventually what I'll see is not the object but pixels. 
The closer I get to an object, 
the more likely is it's just going to dissolve into a whole set of pixels. 
So sensory-motor contingency is this kind of 
combination together of how you perceive and what you perceive. 
The more that that matches, the more that the how matches reality, and 
the more the what you perceive matches what you would expect to see in reality 
through the act of perception. 
So you're getting closer and closer to natural sensory-motor contingencies. 
Now, there's a very big consequence of that. 
If you think about it, if I'm in virtual reality and 
the system affords the natural sensory-motor contingencies so 
that I am perceiving in the virtual world 
much the same way as I do in the real world, what does the brain make of this? 
Really, the simplest hypothesis for the brain to make out of this is, okay, 
this is where I am. 
Because in real life, how do I know where I am? 
Well I look around, I hear, I touch, I see, and I use my body in certain ways. 
If I use my body in the same ways, and 
the same kind of changes to my perception occur, then the simplest hypotheses for 
the brain to make is to give you the illusion that this is where you are. 
The virtual world is where you are. 
So, these sensory-motor contingencies are very very tied up with what we talked 
about right at the beginning, this wow factor. 
I'm somewhere else, I'm not in the lab anymore, I'm in this forest or 
wherever it happens to be. 
>> Yeah, very interesting because it actually reminds me of an examples like 
actually it was the very first time I tried HTC. 
```

### Three Illusions in VR
- Place illusion
- Plausibility illusion
- Body ownership  illusion

#### Place Illusion
Place illusion is strong illusion of being in a place even though you know you’re not there.

Applications of virtual reality in the area of social psychology. 

The bystander problem, you’re somewhere and you see two people fighting and you think of what to do? there's theory that more other people are there, the less likely is that any individual will do anything to help. In Virtual Reality, we can create a situation where where that violent event occurs and because of place illusion, people do have the illusion that they are there and therefore it sparks in them all kinds of similar emotions and feelings that they would have if this was happening in real life.

Different types of immersive system can give rise to the possibility of different types of place illusion, even to the extent that place illusion in some very low level systems, is completely all in your imagination.

So immersion does not cause presence, it does not cause place illusion, it allows the possibility of, and there's different kinds of place illusion that are made possible by different levels of immersive system.

There are three contributors to the place illusion, the illusion that the events are happening for real.
- The first one is that events occur in relation to you personally.
- The second one is that the world responds to you.
- The third one is the credibility.When you're depicting something that could be happening in reality, then it better conform to that



#### Plausibility Illusion

Plausibility Illusion is the illusion, not that you're in the place but what's happening is really happening. So plausibility is the other side of the coin to place illusion. Not only are you there, but what's happening is really happening.

The WOW factor is, "Wow, I feel this is happening even though I know it's not."

## Future of VR in the area of Embodiment

- One of the most important things is that it's kind of contradiction. It's been going for a very, very long time.
- It's been around a long time and it's had these different phases of development.
- We don't know how to tell a story a VR.
- The embodiment is one of the most powerful unique aspects of VR, to have a different body. So somehow that's going to be integrated into the new grammer, the new way of telling stories in VR that won't be able to be told in any other way, in that form except in VR.
- Possibly, the body embodiment is going to be central to the development certainly of narrative story telling in virtual reality, as well as many other aspects.