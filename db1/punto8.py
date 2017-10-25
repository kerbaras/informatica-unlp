from normalizer import normalizer

relation = {'codHospital', 'cantidadHabitaciones', 'direcciónInternacionPaciente', 
            'telefonoInternacionPaciente', 'dniPaciente', 'domicilioPaciente',
            'nombreApellidoPaciente', 'domicilioHospital', 'ciudadHospital',
            'directorHospital', 'fechaInicioInternacion', 'cantDiasIntenacion',
            'doctorQueAtiendePaciente', 'insumoEmpleadoInternació'}

dependencies = [
    ({'dniPaciente'} , {'domicilioPaciente', 'nombreApellidoPaciente'}), 
    ({'codHospital'} , {'domicilioHospital', 'ciudadHospital', 'directorHospital', 'cantidadHabitaciones'}),
    ({'dniPaciente', 'fechaInicioInternacion'} , {'cantDiasIntenacion', 'direcciónInternacionPaciente', 'telefonoInternacionPaciente', 'codHospital'}),
]

normalizer.normalize(relation, dependencies, 'p3p8.md', 8)