gantryAngles = 100
couchAngles = 100
SAD = 90
sourcePoint_bev = [0 -SAD 0];

    % Rotation around Z axis (gantry)
    rotMx_XY_T = [ cosd(gantryAngles) sind(gantryAngles) 0;
                  -sind(gantryAngles) cosd(gantryAngles) 0;
                                           0                         0 1];

    % Rotation around Y axis (couch)
    rotMx_XZ_T = [cosd(couchAngles) 0 -sind(couchAngles);
                                         0 1                        0;
                  sind(couchAngles) 0  cosd(couchAngles)];

    % Rotated Source point (1st gantry, 2nd couch)
     sourcePoint = sourcePoint_bev*rotMx_XY_T*rotMx_XZ_T;
disp("Hello World");

disp(sourcePoint)