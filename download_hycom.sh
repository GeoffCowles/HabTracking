#!/bin/bash

WGET='/usr/bin/wget'

YEAR='2016'
MONTH='01'
DAY='01'
StartSeq='0'
EndSeq='5'

NCSS='http://ncss.hycom.org/thredds/ncss'
MODEL='GLBv0.08'
EXPT='expt_56.3'

VARS="var=surf_el,water_temp,salinity,water_u,water_v"
Subset='spatial=bb'
NORTH='north=47'
SOUTH='south=37'
EAST='east=-60'
WEST='west=-74'

for PlusDay in `seq $StartSeq $EndSeq`; do

  Tstart=`date -d "$YEAR-$MONTH-$DAY +$PlusDay days" +%Y-%m-%dT%H:%M:%SZ`
  echo $Tstart
  Tend=`date -d "$YEAR-$MONTH-$DAY +$PlusDay days + 21 hours" +%Y-%m-%dT%H:%M:%SZ`
  echo ""
  echo ""
  TimeStart="time_start=$Tstart"
  TimeEnd="time_end=$Tend"

  OutFile=$MODEL"_"$EXPT"_`echo $Tstart | cut -d 'T' -f 1`T00Z.nc"
  rm $OutFile

  URL="$NCSS/$MODEL/$EXPT?$VARS&$SPATIAL&$NORTH&$SOUTH&$EAST&$WEST&$TimeStart&$TimeEnd&addLatLon=True"
  echo $URL  
  if [ -s $OutFile ]; then
        echo "[warning] File $OutFile exists (skipping)"
  else
        wget -O $OutFile "$URL"
  fi
done

