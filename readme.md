# Home Assistant Configuration Files 

<p align="center">
  <img src="https://github.com/home-assistant/home-assistant-assets/blob/master/loading-screen.gif">
</p>

<p align="center">
    <a href="https://github.com/robbrad/HA-Config/actions" alt="Pipeline">
        <img src="https://github.com/robbrad/HA-Config/workflows/Home%20Assistant%20CI/badge.svg" /></a>
        <a href="assets/current_ha_version.svg" alt="Currently Running">
        <img src="assets/current_ha_version.svg" /></a>
        <a href="https://www.home-assistant.io/latest-release-notes/" alt="Latest HA Version">
        <img src="https://img.shields.io/badge/dynamic/json?label=Latest%20HA%20Version&query=%24.info.version&url=https%3A%2F%2Fpypi.python.org%2Fpypi%2Fhomeassistant%2Fjson" /></a>
        <a href="https://github.com/robbrad/" alt="Last Commit">
        <img src="https://img.shields.io/github/last-commit/robbrad/HA-Config" /></a>
        <a href="https://github.com/robbrad/HA-Config/stargazers"><img src="https://img.shields.io/github/stars/robbrad/HA-Config.svg?style=plasticr"/></a>     
</p>

<p align="center">
   <a href="https://buymeacoff.ee/robbrad" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
</p>

# Introduction
I discovered [Home Assistant](https://www.home-assistant.io) in 2017 and have been slowly adding to it since then.

## The Home Assistant Server
I run a dedicated Ubuntu 18.04.3 LTS server Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz with 16 gig of ram (This is my main server - I run other things on here as well as Home Assistant)

My setup is a Python Virtual Environment utilising this [guide](https://www.home-assistant.io/docs/installation/virtualenv/).

# Automations
* 

# Hardware Running in my Home Assistant Setup:

# Continuous Integration Continuous Deployment
I use [GitHub Actions](https://github.com/features/actions). When I commit a change to this repo it kicks off an [automatic test](https://github.com/robbrad/HA-Config/actions) of the config using a Home Assistant environment. See [the config here](https://github.com/robbrad/HA-Config/blob/master/.github/workflows/main.yml).

It's very powerful and can run parallel tests on multiple versions of Python and Home Assistant. I currently test Python 3.7 and 3.8 as well as Home Assistant Stable and Beta versions. This helps me know if my config is going to work on a later version before I upgrade.

# HA-Config
My Home Assistant Config

![Alt text](assets/HomeAssistant1.JPG?raw=true "Home Assistant - Home Screen")
![Alt text](assets/HomeAssistant2.JPG?raw=true "Home Assistant - Outside")
![Alt text](assets/HomeAssistant3.JPG?raw=true "Home Assistant - Wifi")
![Alt text](assets/HomeAssistant4.JPG?raw=true "Home Assistant - Automations")


