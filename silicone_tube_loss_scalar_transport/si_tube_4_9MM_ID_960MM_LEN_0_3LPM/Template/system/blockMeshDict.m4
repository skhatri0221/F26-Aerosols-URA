// Parametrized test case for the ERCOFTAC diffuser.

//         Created by Omar Bounous 

//Run using:
//m4 -P blockMeshDict.m4 > blockMeshDict

//m4 definitions:
m4_changecom(//)m4_changequote([,])
m4_define(calc, [m4_esyscmd(perl -e 'use Math::Trig; printf ($1)')])
m4_define(VCOUNT, 0)
m4_define(vlabel, [[// ]Vertex $1 = VCOUNT m4_define($1, VCOUNT)m4_define([VCOUNT], m4_incr(VCOUNT))])

//Mathematical constants:
m4_define(pi, 3.1415926536)

//Geometry
m4_define(wedgeAngle, 1)
m4_define(r1,2.45)

//Grid points (integers!):
m4_define(rNumberOfCells, 25)
m4_define(xABnumberOfCells, 1920)
m4_define(rGrading, 0.2)
m4_define(rGradingY, 10)

//Define planes
m4_define(xA, 0.0)
m4_define(xB, 960)

/*---------------------------------------------------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  1.4.1                                 |
|   \\  /    A nd           | Web:      http://www.openfoam.org               |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

FoamFile
{
    version         2.0;
    format          ascii;

    root            "";
    case            "";
    instance        "";
    local           "";

    class           dictionary;
    object          blockMeshDict;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

convertToMeters 0.001;

vertices
(
//Plane A:
(xA 0 0) vlabel(A0)
(xA calc(r1*cos(deg2rad(wedgeAngle))) -calc(r1*sin(deg2rad(wedgeAngle)))) vlabel(A1)
(xA calc(r1*cos(deg2rad(wedgeAngle))) calc(r1*sin(deg2rad(wedgeAngle)))) vlabel(A2)

//Plane B:
(xB 0 0) vlabel(B0)
(xB calc(r1*cos(deg2rad(wedgeAngle))) -calc(r1*sin(deg2rad(wedgeAngle)))) vlabel(B1)
(xB calc(r1*cos(deg2rad(wedgeAngle))) calc(r1*sin(deg2rad(wedgeAngle)))) vlabel(B2)

);


// Defining blocks:
blocks
(
    //Blocks between plane A and plane B:
    // block0 
    hex (A0 B0 B1 A1 A0 B0 B2 A2) AB
    (xABnumberOfCells rNumberOfCells 1) 
    simpleGrading (1 0.1 1)
   

);

edges
(
    //Plane A:
    arc A1 A2 (xA r1 0)

    //Plane B:
    arc B1 B2 (xB r1 0)



);

// Defining patches:
boundary
(
    axis
    {
	type 	symmetryPlane;
	faces	
	(
		(A0 B0 B0 A0)
	);
    }
    inlet
    {
	type patch;
	faces
	(
		(A0 A2 A1 A0)
	);
    }
    outlet
    {
	type patch;
	faces
	(
		(B0 B1 B2 B0)
	);
    }
    upperWall
    {
	type 	wall;
	faces	
	(

		(A1 A2 B2 B1)
	);
    }

    front
    {
	type wedge;
	neighbourPatch back;
	faces
	(
		(A0 A1 B1 B0)
	);
    }
    back
    {
	type wedge;
	neighbourPatch front;
	faces
	(
		(A2 A0 B0 B2)
	);
    }
);

mergePatchPairs 
(
);

// ************************************************************************* //
