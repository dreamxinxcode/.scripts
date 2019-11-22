#!/bin/bash

echo "Setting wlp3s0 and enp0s25 DOWN.."
sudo ip link set enp0s25 down
sudo ip link set wlp3s0 down

echo "Randomizing wlp3s0 and enp0s25 MAC addresses.."
sudo macchanger -r enp0s25
sudo macchanger -r wlp3s0

echo "Bringing wlp3s0 and enp0s25 UP.."
sudo ip link set enp0s25 up
sudo ip link set wlp3s0 up