case_thickness = 5;
case_depth = 30;
card_height = 32;
card_breadth = 32;
card_width = 2;
cable_width = 19.6;
cable_height = 0.5;

total_height = card_height + (2 * case_thickness);
mount_offset = 5;

module basic_case(height)
linear_extrude(height = height) {
     translate([-2,mount_offset]) mount_point();
     translate([-2,total_height - mount_offset]) mount_point();
     difference() {
          square(size=[case_depth, card_height + (case_thickness * 2)]);
          translate([case_thickness,case_thickness])
               square(size=[case_depth,card_height]);
          translate([20,5]) square(size=[card_width, card_height+1]);
     }
}

module mount_point()
     difference() {
     circle(d=8);
     circle(d=4);
     }

difference() {
     basic_case(card_breadth);
     translate([0, total_height/2, (total_height - cable_width)/3])
          cube([case_thickness, 2, cable_width]);
     }
