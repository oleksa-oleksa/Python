#include <stdio.h>

/* 
To overcome the problem of steady state error for the P controller, 
I controller is being introduced. As its name suggests, the integral 
is merely an accumulated error signals encountered since startup.
Integral = Sum(Error)

This total is multiplied by a constant, Ki, and is added into the loop output.

When the system has already settled down with a small steady state error, 
the integral still continues to accumulate until the CV (control variable) 
is large enough to bring the PV (process variable) inline with SP (set point). 

Just like the P controller, the value of Ki needs to be chosen carefully. 
Too low the value, the steady state error is corrected very slowly; 
too high the value, the system becomes unstable and oscillates.

Because the integral can grow quite large when the set point cannot be reached, 
some applications stop accumulating the error when the CV is saturated.

*/

int main()
{
	while (1) {
		//Get the current position
		current_position = read_current_position();

		//Calculate the error
		error = target_position - current_position;

		// Error accumulation
		integral = integral + error;

		//Calculate the control variable
		control_variable = kp * error + ki * integral;

		// if CV is positive, run the motor clockwise and run forward
		// else run countercockwise and run backward
		if (control_variable > 0) {
			motor_pwm(control_variable);
		}
		else if (control_variable < 0) {
			motor_pwm(-control_variable);
		}
		else {
			motor_stop();
		}
	}
}