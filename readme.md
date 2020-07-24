# Arduino-based Electrotactile Simulation System for Virtual Sensory Contact

Elaborating on the project title, a glove will be worn by a user, 
and mapping of the finger movements will determine whether contact with a virtual object has been made.
Upon contact, the user will experience electrotactile stimulation on their fingertips, sufficient enough to give the impression of touch.

## What is Electrotactile Stimulation (ETS)?
Electrotactile feedback stimulation development is the subject of many research projects, with ideas for use from medicine to the industry and then every day consumers. 
The main idea being to communicate non-tactile information via electrical stimulation of the sense of touch to the user. 

Successful inplementation of electrotactile feedback (ETF) could result in a better standard of living and/or increased experiences and safety in a variety of environments. 
Individuals without the ability to process information in a conventional way, i.e through their eyes, may find that they can still experience the world via ETS.
And in situations where an individual is teleoperating a system where sensation may be of benefit. An elaborate example of this being an astronaut out on a moonwalk.

There are also applications in prosthetics and virtual reality (the underlying basis for this project). 


## Plan

Below is a rough guidline of how I will be going about the creation of a the prototype. 

![Image of project topography](https://github.com/jwilloa/Arduino-based-Electrotactile-Simulation-System-for-Virtual-Sensory-Contact/blob/master/Media/Topography.JPG)

## [Getting Started (Software Based)](https://cseegit.essex.ac.uk/ce301_2019/ce301_willock_j/blob/master/Technical%20Documentation/Getting%20Started%20(Software).md)

You can find the main code [here](https://cseegit.essex.ac.uk/ce301_2019/ce301_willock_j/tree/master/Main%20Python%20Code)

The idea is the use the just the '**Import functions.py**' as the main file. It will access **gloveFunctions.py** to perform certain actions such as read the glove raw data, and vector co-ordinates.

## [Getting Started (Hardware Based)]()

### Pre-requisites
| Topic           | Description  | 
| ---             |  ------  |
| 5DT Data Glove  | Ultra    |   
| LEDs            |          |
| Resitors        |    10k   |
| Capacitors      |    1uF   |
| Wires           |          |
| PCB             |          |
| Arduino Board   |  UNO     |
| Driver/Reciever |  MAX232  |
| Electrodes      |          |

| Software      | Version  | Download Link                                                                                                   |
| ---           |  ------  |---------:                                                                                                       |
| Multisim      |14.1      | [#](https://www.ni.com/en-gb/support/downloads/software-products/download.multisim.html#312060)                 |
| Vizard        |5 (64 Bit)| [#](https://www.worldviz.com/virtual-reality-software-downloads)                                                |

### PCB Board design
Board design will be designed and simulated in Multisim prior to building.

## Author
* Javan Willock - Project Developer
