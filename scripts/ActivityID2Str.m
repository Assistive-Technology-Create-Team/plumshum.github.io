% FallAllD: ActivityID to describtion
% By Majd SALEH 09-April-2020
function res= ActivityID2Str_Short(ActivityID)
res= [];
for i=1:length(ActivityID)
    switch ActivityID(i)
        case 101
            res= [res 'Fall F, walking, trip'];
        case 102
            res= [res 'Fall F, walking, trip, rec.'];
        case 103
            res= [res 'Fall F, walking, slip'];
        case 104
            res= [res 'Fall F, walking, slip, rec.'];
        case 105
            res= [res 'Fall F, walking, slip, rot.'];
        case 106
            res= [res 'Fall F, walking, slip, rot., rec.'];
        case 107
            res= [res 'Fall B, walking, slip'];
        case 108
            res= [res 'Fall B, walking, slip, rec.'];
        case 109
            res= [res 'Fall B, walking, slip, rot.'];
        case 110
            res= [res 'Fall B, walking, slip rot., rec.'];
        case 111
            res= [res 'Fall F, walking, syncope'];
        case 112
            res= [res 'Fall B, walking, syncope'];
        case 113
            res= [res 'Fall L, walking, syncope'];
        case 114
            res= [res 'Fall, syncope, table'];
        case 115
            res= [res 'Fall F, try sit'];
        case 116
            res= [res 'Fall F, try sit, rec.'];
        case 117
            res= [res 'Fall B, try sit'];
        case 118
            res= [res 'Fall B, try sit, rec.'];
        case 119
            res= [res 'Fall L, try sit'];
        case 120
            res= [res 'Fall L, try sit, rec.'];
        case 121
            res= [res 'Fall F, jog, trip'];
        case 122
            res= [res 'Fall F, jog, trip, rec.'];
        case 123
            res= [res 'Fall F, jog, slip'];
        case 124
            res= [res 'Fall F, jog, slip, rev.'];
        case 125
            res= [res 'Fall F, jog, slip, rot.'];
        case 126
            res= [res 'Fall F, jog, slip, rot., rec.'];
        case 127
            res= [res 'Fall L, bed'];
        case 128
            res= [res 'Fall L, bed, rec.'];
        case 129
            res= [res 'Fall F, chair, syncope'];
        case 130
            res= [res 'Fall B, chair, syncope'];
        case 131
            res= [res 'Fall L, chair, syncope'];
        case 132
            res= [res 'Fall F, syncope'];
        case 133
            res= [res 'Fall B, syncope'];
        case 134
            res= [res 'Fall L, syncope'];
        case 135
            res= [res 'Fall, syncope, slide over a wall'];
        % Now ADLs    
        case 1
            res= [res 'Start clap hands'];
        case 2
            res= [res 'Clap hands'];
        case 3
            res= [res 'Stop clap hands'];
        case 4
            res= [res 'Clap hands 1'];
        case 5
            res= [res 'Start wave hands'];
        case 6
            res= [res 'wave hands'];
        case 7
            res= [res 'Stop wave hands'];
        case 8
            res= [res 'Raising hand up'];
        case 9
            res= [res 'Moving hand down'];
        case 10
            res= [res 'Move hand up -> down'];
        case 11
            res= [res 'Hand shaking'];
        case 12
            res= [res 'Beating a table'];
        case 13
            res= [res 'Sitting down'];
        case 14
            res= [res 'Standing up'];
        case 15
            res= [res 'Fail to stand up'];
        case 16
            res= [res 'Lying down'];
        case 17
            res= [res 'Turning while lying'];
        case 18
            res= [res 'Rising up'];
        case 19
            res= [res 'Start walking'];
        case 20
            res= [res 'Walking slowly'];
        case 21
            res= [res 'Stop walking'];
        case 22
            res= [res 'Walking quickly'];
        case 23
            res= [res 'Stumbling'];
        case 24
            res= [res 'Jogging slowly'];
        case 25
            res= [res 'Jogging quickly'];
        case 26
            res= [res 'Jumping slightly'];
        case 27
            res= [res 'Jumping strongly'];
        case 28
            res= [res 'Bending down'];
        case 29
            res= [res 'Start going upstairs'];
        case 30
            res= [res 'Going upstairs'];
        case 31
            res= [res 'Stop going upstairs'];
        case 32
            res= [res  'Start going downstairs'];
        case 33
            res= [res  'Going downstairs'];
        case 34
            res= [res 'Stop going downstairs'];
        case 35
            res= [res 'Upstairs quickly'];
        case 36
            res= [res 'Downstairs quickly'];
        case 37
            res= [res 'Start ascending, lift'];
        case 38
            res= [res 'Stop ascending, lift'];
        case 39
            res= [res 'Start descending, lift'];
        case 40
            res= [res 'Stop descending, lift'];
        case 41
            res= [res 'Standing, moving bus'];
        case 42
            res= [res 'Sitting, moving bus'];
        case 43
            res= [res 'Start jogging'];
        case 44
            res= [res 'Stop jogging'];
        otherwise
            res= [res 'Unknown activity'];
    end
end
end