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
m4_define(openingAngle, 5)
m4_define(wedgeAngle, 1)
m4_define(diffuserLength, 0.16)
m4_define(extensionLength, 0.1)
m4_define(rInOut,5.1054)
m4_define(r2,19)

//Grid points (integers!):
m4_define(rNumberOfCells, 24)
m4_define(xABnumberOfCells, 160)
m4_define(xBCnumberOfCells, 16)
m4_define(xCDnumberOfCells, 16)
m4_define(xDEnumberOfCells, 16)
m4_define(xEFnumberOfCells, 160)
m4_define(xFGnumberOfCells, 240)
m4_define(xGHnumberOfCells, 80)
m4_define(xHInumberOfCells, 32)
m4_define(xIJnumberOfCells, 320)
m4_define(rGrading, 0.2)

//Plane A:
m4_define(xA, 0.0)
m4_define(rA, rInOut)

//Plane B:
m4_define(xB, 100)
m4_define(rB, rInOut)

//Plane C:
m4_define(xC, 102)
m4_define(rC, rInOut)

//Plane D:
m4_define(xD, 104)
m4_define(rD, rInOut)

//Plane E:
m4_define(xE, 106)
m4_define(rE, rInOut)

//Plane F:
m4_define(xF, 130)
m4_define(rF, rInOut)

//Plane G:
m4_define(xG, 247.23)
m4_define(rG, rInOut)

//Plane H:
m4_define(xH, 281.35)
m4_define(rH, rInOut)

//Plane I:
m4_define(xI, 290)
m4_define(rI, rInOut)

//Plane J:
m4_define(xJ, 400)
m4_define(rJ, rInOut)

//Plane K:
m4_define(rF2, r2)
m4_define(rG2, r2)

//Plane L:
m4_define(rH2, r2)

//Plane L:
m4_define(rI2, r2)

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
(xA calc(rA*cos(deg2rad(wedgeAngle))) -calc(rA*sin(deg2rad(wedgeAngle)))) vlabel(A1)
(xA calc(rA*cos(deg2rad(wedgeAngle))) calc(rA*sin(deg2rad(wedgeAngle)))) vlabel(A2)

//Plane B:
(xB 0 0) vlabel(B0)
(xB calc(rB*cos(deg2rad(wedgeAngle))) -calc(rB*sin(deg2rad(wedgeAngle)))) vlabel(B1)
(xB calc(rB*cos(deg2rad(wedgeAngle))) calc(rB*sin(deg2rad(wedgeAngle)))) vlabel(B2)

//Plane C:
(xC 0 0) vlabel(C0)
(xC calc(rC*cos(deg2rad(wedgeAngle))) -calc(rC*sin(deg2rad(wedgeAngle)))) vlabel(C1)
(xC calc(rC*cos(deg2rad(wedgeAngle))) calc(rC*sin(deg2rad(wedgeAngle)))) vlabel(C2)

//Plane D:
(xD 0 0) vlabel(D0)
(xD calc(rD*cos(deg2rad(wedgeAngle))) -calc(rD*sin(deg2rad(wedgeAngle)))) vlabel(D1)
(xD calc(rD*cos(deg2rad(wedgeAngle))) calc(rD*sin(deg2rad(wedgeAngle)))) vlabel(D2)

//Plane E:
(xE 0 0) vlabel(E0)
(xE calc(rE*cos(deg2rad(wedgeAngle))) -calc(rE*sin(deg2rad(wedgeAngle)))) vlabel(E1)
(xE calc(rE*cos(deg2rad(wedgeAngle))) calc(rE*sin(deg2rad(wedgeAngle)))) vlabel(E2)

//Plane F:
(xF 0 0) vlabel(F0)
(xF calc(rF*cos(deg2rad(wedgeAngle))) -calc(rF*sin(deg2rad(wedgeAngle)))) vlabel(F1)
(xF calc(rF*cos(deg2rad(wedgeAngle))) calc(rF*sin(deg2rad(wedgeAngle)))) vlabel(F2)

//Plane G:
(xG 0 0) vlabel(G0)
(xG calc(rG*cos(deg2rad(wedgeAngle))) -calc(rG*sin(deg2rad(wedgeAngle)))) vlabel(G1)
(xG calc(rG*cos(deg2rad(wedgeAngle))) calc(rG*sin(deg2rad(wedgeAngle)))) vlabel(G2)

//Plane H:
(xH 0 0) vlabel(H0)
(xH calc(rH*cos(deg2rad(wedgeAngle))) -calc(rH*sin(deg2rad(wedgeAngle)))) vlabel(H1)
(xH calc(rH*cos(deg2rad(wedgeAngle))) calc(rH*sin(deg2rad(wedgeAngle)))) vlabel(H2)

//Plane I:
(xI 0 0) vlabel(I0)
(xI calc(rI*cos(deg2rad(wedgeAngle))) -calc(rI*sin(deg2rad(wedgeAngle)))) vlabel(I1)
(xI calc(rI*cos(deg2rad(wedgeAngle))) calc(rI*sin(deg2rad(wedgeAngle)))) vlabel(I2)

//Plane J:
(xJ 0 0) vlabel(J0)
(xJ calc(rJ*cos(deg2rad(wedgeAngle))) -calc(rJ*sin(deg2rad(wedgeAngle)))) vlabel(J1)
(xJ calc(rJ*cos(deg2rad(wedgeAngle))) calc(rJ*sin(deg2rad(wedgeAngle)))) vlabel(J2)

//Plane K:
(xF calc(rF2*cos(deg2rad(wedgeAngle))) -calc(rF2*sin(deg2rad(wedgeAngle)))) vlabel(K1)
(xF calc(rF2*cos(deg2rad(wedgeAngle))) calc(rF2*sin(deg2rad(wedgeAngle)))) vlabel(K2)
(xG calc(rG2*cos(deg2rad(wedgeAngle))) -calc(rG2*sin(deg2rad(wedgeAngle)))) vlabel(K3)
(xG calc(rG2*cos(deg2rad(wedgeAngle))) calc(rG2*sin(deg2rad(wedgeAngle)))) vlabel(K4)
);


// Defining blocks:
blocks
(
    //Blocks between plane A and plane B:
    // block0 
    hex (A0 B0 B1 A1 A0 B0 B2 A2) AB
    (xABnumberOfCells rNumberOfCells 1) 
    simpleGrading (rGrading rGrading 1)

    //Blocks between plane B and plane C:
    // block0
    hex (B0 C0 C1 B1 B0 C0 C2 B2) BC
    (xBCnumberOfCells rNumberOfCells 1)
    simpleGrading (rGrading rGrading 1)
    
    //Blocks between plane C and plane D:
    // block0
    hex (C0 D0 D1 C1 C0 D0 D2 C2) CD
    (xCDnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)
    
    //Blocks between plane D and plane E:
    // block0
    hex (D0 E0 E1 D1 D0 E0 E2 D2) DE
    (xDEnumberOfCells rNumberOfCells 1)
    simpleGrading (calc(1/rGrading) rGrading 1)
    
    //Blocks between plane E and plane F:
    // block0
    hex (E0 F0 F1 E1 E0 F0 F2 E2) EF
    (xEFnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)

    //Blocks between plane F and plane G:
    // block0
    hex (F0 G0 G1 F1 F0 G0 G2 F2) FG
    (xFGnumberOfCells rNumberOfCells 1)
    simpleGrading (calc(1/rGrading) rGrading 1)

    //Blocks between plane G and plane H:
    // block0
    hex (G0 H0 H1 G1 G0 H0 H2 G2) GH
    (xGHnumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)

    //Blocks between plane H and plane I:
    // block0
    hex (H0 I0 I1 H1 H0 I0 I2 H2) HI
    (xHInumberOfCells rNumberOfCells 1)
    simpleGrading (1 rGrading 1)

    //Blocks between plane I and plane J:
    // block0
    hex (I0 J0 J1 I1 I0 J0 J2 I2) IJ
    (xIJnumberOfCells rNumberOfCells 1)
    simpleGrading (calc(1/rGrading) rGrading 1)
    
    //Block above the block between plane F and plane G:
    // block0
    hex (F1 G1 K3 K1 F2 G2 K4 K2) FG2
    (xFGnumberOfCells rNumberOfCells 1)
    simpleGrading (calc(1/rGrading) rGrading 1)

);

edges
(
    //Plane A:
    line A0 A1 
    arc A1 A2 (xA rA 0)
    line A2 A0

    //Plane B:
    line B0 B1
    arc B1 B2 (xB rB 0)
    line B2 B0

    //Plane C:
    line C0 C1
    arc C1 C2 (xC rC 0)
    line C2 C0

    //Plane D:
    line D0 D1
    arc D1 D2 (xD rD 0)
    line D2 D0

    //Plane E:
    line E0 E1
    arc E1 E2 (xE rE 0)
    line E2 E0

    //Plane F:
    line F0 F1
    arc F1 F2 (xF rF 0)
    line F2 F0

    //Plane G:
    line G0 G1
    arc G1 G2 (xG rG 0)
    line G2 G0

    //Plane H:
    line H0 H1
    arc H1 H2 (xH rH 0)
    line H2 H0

    //Plane I:
    line I0 I1
    arc I1 I2 (xI rI 0)
    line I2 I0

    //Plane J:
    line J0 J1
    arc J1 J2 (xJ rJ 0)
    line J2 J0

);

// Defining patches:
patches
(
    symmetryPlane axis
    (
        (A0 B0 B0 A0)
        (B0 C0 C0 B0)
        (C0 D0 D0 C0)
        (D0 E0 E0 D0)
        (E0 F0 F0 E0)
        (F0 G0 G0 F0)
        (G0 H0 H0 G0)
        (H0 I0 I0 H0)
        (I0 J0 J0 I0)
    )
    patch inlet
    (
       (A0 A2 A1 A0)
    )
    patch outlet
    (
       (J0 J1 J2 J0)
    )
    wall wallProlongation
    (
      (E1 E2 F2 F1)
    )
    wall wallDiffuser
    (
      (D1 D2 E2 E1)
      (K1 K2 K4 K3)
      (G1 G2 H2 H1)
      (H1 H2 I2 I1)
      (I1 I2 J2 J1)
    )
    wall statSwirlWall
    (
      (B1 B2 C2 C1)
      (C1 C2 D2 D1)
    )
    wall rotSwirlWall
    (
      (A1 A2 B2 B1)
    )
    wedge back
    (
      (A0 A1 B1 B0)
      (B0 B1 C1 C0)
      (C0 C1 D1 D0)
      (D0 D1 E1 E0)
      (E0 E1 F1 F0)
      (F0 F1 G1 G0)
      (G0 G1 H1 H0)
      (H0 H1 I1 I0)
      (I0 I1 J1 J0)
      (F1 G1 K3 K1)
    )
    wedge front
    (
     (A2 A0 B0 B2)
     (B2 B0 C0 C2)
     (C2 C0 D0 D2)
     (D2 D0 E0 E2)
     (E2 E0 F0 F2)
     (F2 F0 G0 G2)
     (G2 G0 H0 H2)
     (H2 H0 I0 I2)
     (I2 I0 J0 J2)
     (F2 G2 K4 K2)
     )
);

mergePatchPairs 
(
);

// ************************************************************************* //
