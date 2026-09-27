mesh: 
	( cd system && m4 -P blockMeshDict.m4 > blockMeshDict)
	( blockMesh  | tee log.blockMesh)

run:
	( decomposePar )
	( mpirun -np 4 simpleFoam -parallel )
	( reconstructPar -latestTime )
	( postProcess -funcs '(components(U))' -latestTime )
	( postProcess -func sampleDict -latestTime )

runScalar:
	( cp -r constant/polyMesh scalarTransport/constant/ )
	( latestTime=$$(foamListTimes -latestTime) && cp $$latestTime/U scalarTransport/0/)
	( latestTime=$$(foamListTimes -latestTime) && cp $$latestTime/p scalarTransport/0/)
	( latestTime=$$(foamListTimes -latestTime) && cp $$latestTime/phi scalarTransport/0/)
	( latestTime=$$(foamListTimes -latestTime) && cp $$latestTime/nut scalarTransport/0/)	
	( cd scalarTransport && scalarTransportFoamEff)

clean: 
	( ./Allclean )

view: 
	( paraFoam & )

###############







