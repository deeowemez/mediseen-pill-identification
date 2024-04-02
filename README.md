# Pill Identification System Readme

** This is an ongoing project

## Overview
The Pill Identification System is a Raspberry Pi 4B-based solution designed to streamline the process of identifying medications. It captures an image of a pill placed within a 3d printed enclosure, processes the images, runs an inference and outputs detailed information about the pill on both display and audio channels. The system also features push buttons for volume control and reclassification, a battery level indicator for portable power supply, and an RGB LED indicator for status feedback.

## Features
- Image Capture: Utilizes a 2.1MP USB camera module to capture pill images
- Image Processing: Image processing algorithms analyze the captured images to identify the pill based on its shape, color, and markings.
- Display Output: Provides detailed information about the identified pill on a display screen, including the medication name, dosage, special instructions, and potential side effects.
- Audio Output: Delivers a TTS audio output, announcing the identified pill information for accessibility and convenience.
- Push Buttons: Volume control buttons allow users to adjust audio output volume, while a reclassify button enables reclassification of the current pill in pill slot.
- Battery Level Indicator: Displays the remaining battery level of the portable power supply.
- RGB LED Indicator: Provides visual feedback on the system status, indicates the following colors:
	white color - after booting up,
	cyan color - during pill detection and inference, 
	red color - in case of classification errors, and 
	green color - upon successful classification.
- 3d printed enclosure: The system is integrated into a 3d printed enclosure designed with designated pill slot to securely hold pills for identification.

## List of Pills
The following are the list of pills included in the database for creating the image classification model and can be recognized by the system:

	1. Diamicron MR Gliclazide 60mg (Packed)
	2. Diamicron MR Gliclazide 60mg (Unpacked)
	3. Getryl Glimepiride 2mg (Unpacked)
	4. Glucophage Metformin HCl 1g (Packed)
	5. Glucophage Metformin HCl 1g (Unpacked)
	6. Glucophage XR Metformin HCl 750mg (Packed)
	7. Glucophage XR Metformin HCl 750mg (Unpacked)
	8. Jardiance FC Empagliflozin 10mg (Packed)
	9. Jardiance FC Empagliflozin 10mg (Unpacked Side A)
	10. Jardiance FC Empagliflozin 10mg (Unpacked Side B)
	11. Jardiance FC Empagliflozin 25mg (Packed)
	12. Jardiance FC Empagliflozin 25mg (Unpacked Side A)
	13. Jardiance FC Empagliflozin 25mg (Unpacked Side B)
	14. RiteMed Gliclazide 80mg (Packed)
	15. RiteMed Gliclazide 80mg (Unpacked)
	16. RiteMed Glimepiride 2mg (Packed)
	17. RiteMed Glimepiride 2mg (Unpacked)
	18. Sucranorm Metformin HCl 850mg (Packed)
	19. Sucranorm Metformin HCl 850mg (Unpacked)
	20. TGP Gliclazide 80mg (Packed)
	21. TGP Gliclazide 80mg (Unpacked)
	22. Trajenta Duo Linagliptin Metformin HCl 1g (Unpacked Side A)
	23. Trajenta Duo Linagliptin Metformin HCl 1g (Unpacked Side B)
	24. Trajenta Duo Linagliptin Metformin HCl 500mg (Unpacked Side A)
	25. Trajenta Duo Linagliptin Metformin HCl 500mg (Unpacked Side B)
	26. Velmetia Sitagliptin Metformin HCl 1g (Unpacked)
	27. Velmetia Sitagliptin Metformin HCl 500mg (Unpacked)
	28. Zoliget Glimepiride 30mg (Unpacked)

## Getting Started
To set up the Pill Identification System, follow these steps:
1. Assemble the RPi4 and camera according to the provided instructions.
2. Install the necessary software and dependencies onto the RPi4.
3. Connect the USB camera to the RPi4 port 0.
4. Place the pill to be identified within the pill slot inside the enclosure.
5. The system will automatically run inference upon detection of the presence of a pill.
6. View the display output and listen to the audio output to obtain information about the identified pill.
7. Use the push buttons for volume control and reclassification as needed.
8. Monitor the battery level indicator for portable power supply status.
9. Refer to the RGB LED indicator for system status feedback.


## Technologies Used
- Raspberry Pi 4B: Embedded computing platform serving as the core of the system.
- USB Camera Module: Captures images of pills for identification.
- Image Processing Algorithms: Analyze pill images for identification.
- Display Screen: Presents detailed pill information.
- Audio Output: Announces identified pill information audibly.
- Push Buttons: Enable volume control and reclassification functionalities.
- Battery Level Indicator: Displays remaining battery level of the portable power supply.
- RGB LED Indicator: Provides visual feedback on system status.

## Acknowledgments
- Project Contributors: Ire Ann De Guzman, Marianne Domilies, Kirsty Viviene Ducusin, Ernestine Gail Dulce, Russell Nixon Rivera, Alexie Sobrepena, Jericho Agonoy, Charles Fontanilla
(https://github.com/deeowemez/pill-identification/assets/53809101/ba492d17-93c6-4de8-a480-cdf835196fae)
