# 3.2_Touchsy_HAT_Resistive_Software

Touchsy HAT - the perfect solution for users who want to mount the display on their single-board computers. This github includes software, library and getting started instruction with details of Touchsy HAT board details.

A HAT for Raspberry Pi, a Raspberry Pi Pico-based display module, an ESP-32-based display module, and a display breakout to address additional single-board computers are available. These models are available in both capacitive and resistive versions.

<img src="https://cdn.shopify.com/s/files/1/1217/2104/files/TOUCHSYHAT_BANNER.jpg?v=1688107978">

Here are the features and specifications that make Touchsy HAT a unique and must-have accessory for Raspberry Pi 4, 3, and other compatible single-board computers:
### Features:
- Resistive touchscreen technology for accurate and responsive touch input
- 3.2" high-quality visuals display size that perfectly fits the size of Pi 4
- 5-way joystick support for versatile control options
- 2 programmable buttons that can be customized for various functions
- The programmable multi-tune buzzer can alert you to notifications or other events
- Compatible with Raspberry Pi 4, 3, and other 40 Pin GPIO compatible single-board computers

### Specifications:
- Operating voltage 3.3V 
- 3.2” Display with resolution 320 × 240
- XPT2046 resistive touch controller 
- ILI9341 Display Driver
- Appearance: RGB
- Colors: 65K/262K
- Viewing Angle(in degree): Left:70, Right:70, Up:50, Down:70 
- Operating Temperature is -20℃~70℃
- Storage Temperature is -30℃~80℃

## Hardware Overview:
<img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/Touchsy%20hat%20pinout.jpg">

- (1) 5-Way Joystick
- (2) & (4) programmable buttons
- (3) 3.2” Resistive Touch Display
- (5) Buzzer
- (6) GPIO Header (to connect Pi and other SBC’s)

**HAT and Raspberry Pi Pins Mapping Detail**
  
  <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/Touchsy%20Hat%20with%20RPi%20pin%20Map.png">

  _Display and Touch Control Pins:_
  | Symbol | Description |
  |---|---|
  | CS0 | Display control Chip select pin for SPI bus interfacing |
  | CS1  | Touch control Chip select pin for SPI bus interfacing | Clock pin for SPI interfacing
  | CLK | SPI Clock Pin for both Touch & Display |
  | D/C | Data/Command pin of Display, Logic HIGH for Data and Logic LOW for Command   |
  | DIN  | Data In (MOSI) pin to both Display and Touch for SPI interfacing |
  | DOUT | Touch control Data Out (MISO) pin for SPI interfacing |
  | LCD_IRQ | Touch Controller Interrupt pin, Logic LOW when touch detected |
  | RESET | Display Reset pin |
  | BL | BackLight for Display panel |
  
   _Actuator Pins:_
  | Symbol | Description | 
  |---|---|
  | BUZZER  | Buzzer device control pin | 
  | BT1 | Programmable Button 1 |
  | BT2 | Programmable Button 2 |
  | JOY RIGHT | 5-WAY Joy Stick Switch pin|
  | JOY UP | 5-WAY Joy Stick Switch pin|
  | JOY DOWN | 5-WAY Joy Stick Switch pin|
  | JOY SEL | 5-WAY Joy Stick Switch pin|
  | JOY LEFT | 5-WAY Joy Stick Switch pin|
  
   _Power Pins:_
  | Symbol | Description | 
  |---|---|
  | 5V  | 5V Input Supply |
  | GND | Common Supply Ground pin |

## Setup steps to Configure Touchsy HAT for Raspberry Pi
### Step 1: Download and install Raspberry OS to Pi
  - Follow the Getting Started [Link](https://www.raspberrypi.com/documentation/computers/getting-started.html) to perform OS install 
  - Now you can either use Screen and Keyboard to access Pi or Setup to use [remotely with VNC viewer](https://projects.raspberrypi.org/en/projects/infrared-bird-box/13).

### Step 2: Configure Touchsy HAT
  - Connect Touchsy HAT to raspberry Pi as shown in [pin mapping section](https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/raw/main/images/Touchsy%20Hat%20with%20RPi%20pin%20Map.png)
  - Download this github into Raspberry Pi by typing following command into Terminal
    ```
    git clone https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/
    ```
    <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/g1.png" width="533" height="336">
  - Check if folder downloaded, then just rename folder Touchsy_HAT as shown in below images
    <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/g2.png" width="533" height="336">
    <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/g3.png" width="533" height="336">
    <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/g4.png" width="533" height="336">
  - Open Terminal and run following commands to setup
    ```
    cd Touchsy_HAT
    ```
    ```
    sudo chmod 777 *
    ```
    ```
    sudo ./Touchsy_HAT 0
    ```
    <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/t1.png" width="533" height="336">
   
    <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/t2.png" width="533" height="336">

    <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/t3.png" width="533" height="336">
    
    Note: We have kept default angle of screen 0 degree, you can change as 90, 180 or 270 as per requirement. E.g.shown below
    ```
    sudo ./Touchsy_HAT 90
    ```

    Raspberry Pi will restart after this command and screen resolution will be change as per HAT, 240 x 320 pixel, shown below.
    
    <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/t4.png" width="533" height="336">
    <img src="https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/t5.png" width="533" height="336">

## Testing 5-way Switch, Programmable Button & Buzzer  
  - You will find example python code as [Button_Buzzer_demo.py](https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/Button_Buzzer_demo.py) in this repo. 
  - Run this code using default python IDE or thonny IDE. This helps to check basic working demo of programmable switches, 5-way switch and Buzzer available on Touchsy HAT. So you can use them to build some automation or add additional functionality to your project.
    
    <img src = "https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Software/blob/main/images/run_democode.png" width="812" height="413">
    
## Resources
**3.2" Touchsy HAT Resistive :** 
  * [Schematic](https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Hardware/blob/main/Design%20Data/Sch%203.2%20INCH%20Touchsy%20HAT(Resistive).pdf)
  * [Step File](https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Hardware/blob/main/Mechanical%20Data/step%203.2%20INCH%20Touchsy%20HAT(Resistive)%2012042023.step)
  * [Hardware Files](https://github.com/sbcshop/3.2_Touchsy_HAT_Resistive_Hardware)
    
**Other Related :**
  * [Getting Started With Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
  * [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)


## Related Products
   * [3.2" Touchsy ESP32](https://shop.sb-components.co.uk/collections/pre-order/products/touchsy-3-2-touch-lcd-display-based-on-esp32-mcu) - 3.2" Touchsy ESP32 with Resistive and Capacitive version. 
   * [3.2" Touchsy Pico W](https://shop.sb-components.co.uk/collections/pre-order/products/touchsy-3-2-touch-lcd-display-based-on-pico-w) - 3.2" Touchsy Pico W with Resistive and Capacitive version.
   * [3.2" Touchsy Breakout](https://shop.sb-components.co.uk/collections/pre-order/products/touchsy-3-2-touch-lcd-display-breakout-board) - 3.2" Touchsy Breakout with Resistive and Capacitive version.
   * [3.2" Touchsy HAT](https://shop.sb-components.co.uk/collections/pre-order/products/touchsy-3-2-touch-lcd-display-for-raspberry-pi) - 3.2" Touchsy HAT with Resistive version for Raspberry Pi.
   * [1.28" Round Touch LCD HAT](https://shop.sb-components.co.uk/products/1-28-round-touch-lcd-hat-for-raspberry-pi?_pos=2&_sid=6c0f5891d&_ss=r) - 1.28" Round Touch LCD HAT for Raspberry Pi.

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>

