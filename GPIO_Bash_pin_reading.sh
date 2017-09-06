# @wickey:/sys/class/gpio $ echo "20" > /sys/class/gpio/export 
# pi@wickey:/sys/class/gpio $ echo "out" > /sys/class/gpio/gpio20/direction 
# pi@wickey:/sys/class/gpio $ echo "1" > /sys/class/gpio/gpio20/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio20/value 
# pi@wickey:/sys/class/gpio $ echo "21" > /sys/class/gpio/export 
# pi@wickey:/sys/class/gpio $ echo "16" > /sys/class/gpio/export 
# pi@wickey:/sys/class/gpio $ echo "12" > /sys/class/gpio/export 
# pi@wickey:/sys/class/gpio $ echo "15" > /sys/class/gpio/export 
# pi@wickey:/sys/class/gpio $ echo "14" > /sys/class/gpio/export 
# pi@wickey:/sys/class/gpio $ echo "out" > /sys/class/gpio/gpio21/direction 
# pi@wickey:/sys/class/gpio $ echo "out" > /sys/class/gpio/gpio16/direction 
# pi@wickey:/sys/class/gpio $ echo "out" > /sys/class/gpio/gpio12/direction 
# pi@wickey:/sys/class/gpio $ echo "out" > /sys/class/gpio/gpio15/direction 
# pi@wickey:/sys/class/gpio $ echo "out" > /sys/class/gpio/gpio14/direction 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio21/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio20/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio26/value 
# -bash: /sys/class/gpio/gpio26/value: No such file or directory
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio16/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio12/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio15/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio14/value 
# pi@wickey:/sys/class/gpio $ echo "255" > /sys/class/gpio/gpio14/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio14/value 
# pi@wickey:/sys/class/gpio $ echo "1" > /sys/class/gpio/gpio14/value 
# pi@wickey:/sys/class/gpio $ echo "255" > /sys/class/gpio/gpio14/value 
# pi@wickey:/sys/class/gpio $ echo "255" > /sys/class/gpio/gpio14/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio14/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio21/value 
# pi@wickey:/sys/class/gpio $ echo "1" > /sys/class/gpio/gpio21/value 
# pi@wickey:/sys/class/gpio $ echo "2" > /sys/class/gpio/gpio21/value 
# pi@wickey:/sys/class/gpio $ echo "5" > /sys/class/gpio/gpio21/value 
# pi@wickey:/sys/class/gpio $ echo "255" > /sys/class/gpio/gpio21/value 
# pi@wickey:/sys/class/gpio $ echo "0" > /sys/class/gpio/gpio21/value 
# pi@wickey:/sys/class/gpio $ echo "1" > /sys/class/gpio/gpio21/value 
# pi@wickey:/sys/class/gpio $ echo "1" > /sys/class/gpio/gpio22/value 
# -bash: /sys/class/gpio/gpio22/value: No such file or directory
# pi@wickey:/sys/class/gpio $ echo "1" > /sys/class/gpio/gpio20/value 
# pi@wickey:/sys/class/gpio $ 
echo "0" > /sys/class/gpio/gpio26/value 