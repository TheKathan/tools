#!/usr/bin/expect -f

set dir [lindex $argv 0];
set hostname [lindex $argv 1];

# connect via scp
spawn scp -r $dir pi@stanny:/media/STANNYHD/faces/$hostname/
#######################
expect {
  -re ".*es.*o.*" {
    exp_send "yes\r"
    exp_continue
  }
  -re ".*sword.*" {
    exp_send "raspberry\r"
  }
}
#######################

interact
