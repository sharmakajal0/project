# Realism

## Graphics
Challenges in rendering realistic looking graphics in VR.

In lot of applications, it is overly important to create realistic looking graphical representions of the world. For instance, in training and therapy, if the graphics do no reflect the world, then the skills acquired in VR won't be transferable. The graphics should like they look in a photo, so that's why the term photorealistic to describe those virtual environments.

Other times we might want to create an imaginary fantasy world, but this doesn't mean we no longer care about realism altogether. We still want the users to somehow understand and connect with that world. In order for this to happen, objects have to interact with lighting in similar way as they do in real life. For instance, water ships do reflect lights in a certain way so that we perceive it as water.

In order to create an environment that looks photorealistic or at least reflect to a certain degree how the real world works, we need to have a basic idea of how lighting works in real life. If you look around, you see that light interacts with objects in different ways.

Diffuse reflection is computationally cheaper to produce but specular reflection is a bit more mathematically complicated so we say it is more expensive to render. 

If we don't render any lighting effects in VR things can look a bit flat rather than 3D.

The most computationally expensive images to produce are glossy or mirror surfaces. These are surfaces you can see through or surfaces that reflect things around them. They are often considered to be examples of specular reflection. These are all possible to render in VR, but normally at a very high cost.

While you are planning to illuminate your VR environment, there are three types of surface you will need to deal with:
- diffuse(fabric)
- specular(metal)
- glossy / mirror
```
Diffused surfaces are cheapest to render.

Specular surfaces are little more complex.

Glossy or mirror surfaces are very expensive.
```
When we talk about illumination realism in VR, we mean how lights are reflected on the 3D objects. This is important in creating a realistic and believable environment. There are also practical functions.

Sometimes it is difficult to pin down exactly what an image is missing.

In local illumination, we only consider lights that come directly from the light source.

In global illumination, we also consider inter-reflection between objects. So basically global illumination creates more realistic environments, but it is more computationally expensive.


It means in order to render real-time graphics in VR while maintaining the required high frame rate, we will have to turn off the global illumination.

## Animation

`Challenges of creating realistic and believable animation in VR`

Any animation would feel real if it is moving like it is in real life. And this is little too difficult to animate. It need a lot of programming and computation.

The good news is that most game engines nowadays come with built in physics engine that takes care of physical simulations.

Another powerful animation tool taht often comes as part of a game engine is called particle system. It often used to generate effects, such as smoke, fire, and snow.

A lot of the challenges in creating believable virtual character's animations in VR overlap with the ability of the users to interact with them.

Animation is not a problem with most 360-degree videos. But the problem is that the only thing you can do once you've captured a video is cut and resequence the video clips. You cannot manipulate objects in the footage like you can with model-based VR. So you would not be able to program the real human actors in the video to rotate their heads to follow the user, at least not in a naturalistic way.

## Navigation

With high-end devices which support position tracking, you can shift your body naturally to see what's behind an object in front of you. And walk around with your legs just like you do in real life.

On the other hand, in mobile VR as there is no position tracking, most of the time you'll need to use the VR controllers for both, to shift your view point or to move to a different place. 

Not all VR applications require the user to move around that much.

#### Physical Navigation
If you need your participants to walk around in the VR space, the best way is for them to move around exactly the same way as they do in real life. This is often called physical navigation.

- The problem with this is that you are limited by the physical space you're in.
- Another problem is obviously that it won't work with mobile VR devices as we cannot track where a user is in the 3D space.

#### Virtual Navigation
The other extreme is to use virtual navigation where users control their movements entirely using the joystick or touch pad that comes with their VR controllers.

In 360 video, the user only has access to view the environment from the fixed precision where you filmed with your camera.

There's a method called walk-in-place. Participants walk-in-place by doing the walking motion with their legs without actually moving forward.

They could also use their arms to indicate the direction of turning. The participant's body is tracked by a Microsoft Kinect Sensor, but you can use the VR controllers to try to do something similar. 

#### Teleporting

Another method to move from one place to another, which is called Teleportation. Basically, there are a few fixed positions the users can choose to teleport themselves to.

In 360 video, the users cannot navigate the environment freely, but some 360 video allows the users to teleport, for example, Google Street View.

##### comparison
In all the methods we use, physical navigation is the most natural one, but it is constrained by the physical space the user is in.

Walk-in-place is less natural, and it gives no sense of acceleration but it does not normally cause nausea.

Teleporting is a good way to move around quickly in VR without making the user feel too dizzy. But the user often gets disoriented when they land in a new location.

Virtual Navigation which lies entirely on a 2D user interface, that is, the joystick or touchpad is not encouraged as it causes nausea.


## Nausea

Nausea in VR is also called simulation sickness, whick refers to the discomfort induced by simulated environments.

Its mainly caused by the conflict between information received in the brain from our vestibular system and our visual system. 

In this situation, you are physically moving while looking at something relatively still. So your vestibular system tells the brain that you are moving, but your visual system says you're not and that's what makes you feel sick.

With simulation sickness, it's almost the opposite.

The best ways to avoid simulation sickness is to pay attention to how users could navigate in the virtual environment. Physical movements where users use their own body to move around in VR just like they do in real life tend not to cause much nausea, if any at all.

If you don't want to limit user movement by their physical space, you could consider methods such as walk in place or teleporting.

The worst method is to directly import the first person controller used in many games, where users can move around with the keyboard and mouse and a joystick.

There are other factors that contribute to simulation sickness in VR.

Because the displays are very close to your eyes, you might experience eye strain.

A frame rate below 90 hertz per second could cause discomfort as could flashing or high contrast images.

So these are the things you might want to avoid when building your VR environments.

