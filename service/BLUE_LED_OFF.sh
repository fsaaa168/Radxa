#!/bin/sh
i=0

for ((i=0;i<20;i++))
do
echo 0 > /sys/class/gpio/gpio174/value #led on
sleep 0.009
echo 1 > /sys/class/gpio/gpio174/value #led off
sleep 0.001
done

for ((i=0;i<20;i++))
do
echo 0 > /sys/class/gpio/gpio174/value #led on
sleep 0.008
echo 1 > /sys/class/gpio/gpio174/value #led off
sleep 0.002
done

for ((i=0;i<20;i++))
do
echo 0 > /sys/class/gpio/gpio174/value #led on
sleep 0.007
echo 1 > /sys/class/gpio/gpio174/value #led off
sleep 0.003
done

for ((i=0;i<20;i++))
do
echo 0 > /sys/class/gpio/gpio174/value #led on
sleep 0.006
echo 1 > /sys/class/gpio/gpio174/value #led off
sleep 0.004
done

for ((i=0;i<20;i++))
do
echo 0 > /sys/class/gpio/gpio174/value #led on
sleep 0.005
echo 1 > /sys/class/gpio/gpio174/value #led off
sleep 0.005
done
for ((i=0;i<20;i++))
do
echo 0 > /sys/class/gpio/gpio174/value #led on
sleep 0.004
echo 1 > /sys/class/gpio/gpio174/value #led off
sleep 0.006
done

for ((i=0;i<20;i++))
do
echo 0 > /sys/class/gpio/gpio174/value #led on
sleep 0.003
echo 1 > /sys/class/gpio/gpio174/value #led off
sleep 0.007
done

for ((i=0;i<20;i++))
do
echo 0 > /sys/class/gpio/gpio174/value #led on
sleep 0.002
echo 1 > /sys/class/gpio/gpio174/value #led off
sleep 0.008
done

for ((i=0;i<20;i++))
do
echo 0 > /sys/class/gpio/gpio174/value #led on
sleep 0.001
echo 1 > /sys/class/gpio/gpio174/value #led off
sleep 0.009
done