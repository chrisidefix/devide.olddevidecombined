#include "ivconv.h"

bool IVCONV::wrl_write ( FILE *fileout )

/**********************************************************************/

/*
Purpose:

WRL_WRITE writes graphics data to a WRL file.

Example:

#VRML V2.0 utf8

WorldInfo {
title "cube.iv."
string "WRL file generated by IVREAD.
}

Group {
children [

Shape {

appearance Appearance {
material Material {
diffuseColor   0.0 0.0 0.0
emissiveColor  0.0 0.0 0.0
shininess      1.0
}
} #end of appearance

geometry IndexedLineSet {

coord Coordinate {
point [
8.59816       5.55317      -3.05561
8.59816       2.49756      0.000000E+00
...etc...
2.48695       2.49756      -3.05561
]
}

coordIndex [
0     1     2    -1     3     4     5     6     7     8    -
9    10    -1    11    12    -1    13    14    15    -1    1
...etc...
191    -1
]

colorPerVertex TRUE

colorIndex [
0     0     0    -1     2     3     1     1     4     7    -
10     9    -1     7     7    -1     3     2     2    -1    1
...etc...
180    -1
]

}  #end of geometry

}  #end of Shape

]  #end of children

}  #end of Group

Modified:

23 May 1999

Author:

John Burkardt
*/
{
	int icor3;
	int iface;
	int ivert;
	int j;
	int ndx;
	
	text_num = 0;
	
	fprintf ( fileout, "#VRML V2.0 utf8\n" );
	fprintf ( fileout, "\n" );
	fprintf ( fileout, "  WorldInfo {\n" );
	fprintf ( fileout, "    title \"%s\"\n", fileout_name );
	fprintf ( fileout, "    info \"WRL file generated by IVREAD.\"\n" );
	fprintf ( fileout, "    info \"Original data in %s\"\n", filein_name );
	fprintf ( fileout, "  }\n" );
	fprintf ( fileout, "\n" );
	fprintf ( fileout, "  Group {\n" );
	fprintf ( fileout, "    children [\n" );
	fprintf ( fileout, "      Shape {\n" );
	fprintf ( fileout, "        appearance Appearance {\n" );
	fprintf ( fileout, "          material Material {\n" );
	fprintf ( fileout, "            diffuseColor   0.7 0.7 0.7\n" );	// default color non black (PhG)
	fprintf ( fileout, "            emissiveColor  0.7 0.7 0.7\n" );
	fprintf ( fileout, "            shininess      1.0\n" );
	fprintf ( fileout, "          }\n" );
	fprintf ( fileout, "        }\n" );
	
	++text_num;
	/*
	IndexedLineSet
	*/
	if ( line_num > 0 ) {
		
		fprintf ( fileout, "        geometry IndexedLineSet {\n" );
		/*
		IndexedLineSet coord
		*/
		fprintf ( fileout, "          coord Coordinate {\n" );
		fprintf ( fileout, "            point [\n" );
		
		text_num = text_num + 3;
		
		for ( icor3 = 0; icor3 < cor3_num; icor3++ ) {
			fprintf ( fileout, "              %f %f %f\n", cor3[icor3][0],
				cor3[icor3][1], cor3[icor3][2] );
			++text_num;
		}
		
		fprintf ( fileout, "            ]\n" );
		fprintf ( fileout, "          }\n" );
		text_num = text_num + 2;
		/*
		IndexedLineSet coordIndex.
		*/
		fprintf ( fileout, "          coordIndex [\n" );
		
		++text_num;
		
		for ( j = 0; j < line_num; ++j ) {
			fprintf ( fileout, "%d ", line_dex[j] );
			if ( line_dex[j] == -1 || j == line_num - 1 ) {
				fprintf ( fileout, "\n" );
				++text_num;
			}
		}
		
		fprintf ( fileout, "          ]\n" );
		++text_num;
		/*
		Colors. (materials)
		*/
		fprintf ( fileout, "          color Color {\n" );
		fprintf ( fileout, "            color [\n" );
		text_num = text_num + 2;
		
		for ( j = 0; j < material_num; ++j ) {
			fprintf ( fileout, "              %f %f %f\n", material[j].rgb[0],material[j].rgb[1],material[j].rgb[2]);
			++text_num;
		}
		
		fprintf ( fileout, "            ]\n" );
		fprintf ( fileout, "          }\n" );
		fprintf ( fileout, "          colorPerVertex TRUE\n" );
		/*
		IndexedLineset colorIndex
		*/
		fprintf ( fileout, "          colorIndex [\n" );
		
		text_num = text_num + 4;
		
		for ( j = 0; j < line_num; ++j ) {
			fprintf ( fileout, "%d ", line_material[j] );
		}
		fprintf ( fileout, "\n" );
		++text_num;
		
		fprintf ( fileout, "          ]\n" );
		fprintf ( fileout, "        }\n" );
		text_num = text_num + 2;
		
	}
	/*
	End of IndexedLineSet
	
	  IndexedFaceSet
	*/
	if ( face_num > 0 ) {
		
		fprintf ( fileout, "        geometry IndexedFaceSet {\n" );
		/*
		IndexedFaceSet coord
		*/
		fprintf ( fileout, "          coord Coordinate {\n" );
		fprintf ( fileout, "            point [\n" );
		
		text_num = text_num + 3;
		
		for ( icor3 = 0; icor3 < cor3_num; icor3++ ) {
			fprintf ( fileout, "              %f %f %f\n", cor3[icor3][0],
				cor3[icor3][1], cor3[icor3][2] );
			
			++text_num;
		}
		
		fprintf ( fileout, "            ]\n" );
		fprintf ( fileout, "          }\n" );
		/*
		IndexedFaceSet coordIndex.
		*/
		fprintf ( fileout, "          coordIndex [\n" );
		
		text_num = text_num + 3;
				
		for ( iface = 0; iface < face_num; iface++ ) {
			
			for ( ivert = 0; ivert < face_order[iface]; ivert++ ) {
				fprintf ( fileout, "%d ", face[ivert][iface]);
			}
			fprintf ( fileout, "%d ", -1);
			fprintf ( fileout, "\n" );
			++text_num;
		}
		
		fprintf ( fileout, "          ]\n" );
		++text_num;
		/*
		IndexedFaceset colorIndex
		*/
		fprintf ( fileout, "          colorIndex [\n" );
		++text_num;
		
		ndx = 0;
		
		for ( iface = 0; iface < face_num; iface++ ) {
			
			for ( ivert = 0; ivert < face_order[iface]; ivert++ ) {
				fprintf ( fileout, "%d ", vertex_material[ivert][iface] );
			}
				
			fprintf ( fileout, "%d ", -1 );
			fprintf ( fileout, "\n" );
			++text_num;
		}
		
		fprintf ( fileout, "          ]\n" );
		fprintf ( fileout, "        }\n" );
		text_num = text_num + 2;
		
	}
	/*
	End of IndexedFaceSet
	
	  End of:
	  Shape
	  children
	  Group
	  */
	  fprintf ( fileout, "      }\n" );
	  fprintf ( fileout, "    ]\n" );
	  fprintf ( fileout, "  }\n" );
	  
	  text_num = text_num + 3;
	  /*
	  Report.
	  */
	  printf ( "\n" );
	  printf ( "WRL_WRITE - Wrote %d text lines.\n", text_num );
	  
	  return true;
}
/******************************************************************************/

