#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Procedure) on 2015-09-24.
#  2015, SMART Health IT.


from . import annotation
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period


class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.
    
    An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """
    
    resource_name = "Procedure"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySite = None
        """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ The encounter associated with the procedure.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.focalDevice = None
        """ Device changed in procedure.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """
        
        self.followUp = None
        """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the procedure happened.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.notPerformed = None
        """ True if procedure was not performed as scheduled.
        Type `bool`. """
        
        self.notes = None
        """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performedDateTime = None
        """ Date/Period the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.performedPeriod = None
        """ Date/Period the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Reason procedure performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonNotPerformed = None
        """ Reason procedure was not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason procedure performed.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.report = None
        """ Any report resulting from the procedure.
        List of `FHIRReference` items referencing `DiagnosticReport` (represented as `dict` in JSON). """
        
        self.request = None
        """ A request for this procedure.
        Type `FHIRReference` referencing `CarePlan, DiagnosticOrder, ProcedureRequest, ReferralRequest` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | aborted | completed | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Who the procedure was performed on.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        self.used = None
        """ Items used during procedure.
        List of `FHIRReference` items referencing `Device, Medication, Substance` (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True),
            ("category", "category", codeableconcept.CodeableConcept, False),
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("complication", "complication", codeableconcept.CodeableConcept, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True),
            ("followUp", "followUp", codeableconcept.CodeableConcept, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("location", "location", fhirreference.FHIRReference, False),
            ("notPerformed", "notPerformed", bool, False),
            ("notes", "notes", annotation.Annotation, True),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False),
            ("performedDateTime", "performedDateTime", fhirdate.FHIRDate, False),
            ("performedPeriod", "performedPeriod", period.Period, False),
            ("performer", "performer", ProcedurePerformer, True),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False),
            ("reasonNotPerformed", "reasonNotPerformed", codeableconcept.CodeableConcept, True),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False),
            ("report", "report", fhirreference.FHIRReference, True),
            ("request", "request", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("used", "used", fhirreference.FHIRReference, True),
        ])
        return js


class ProcedureFocalDevice(fhirelement.FHIRElement):
    """ Device changed in procedure.
    
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """
    
    resource_name = "ProcedureFocalDevice"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manipulated = None
        """ Device that was changed.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        super(ProcedureFocalDevice, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False),
            ("manipulated", "manipulated", fhirreference.FHIRReference, False),
        ])
        return js


class ProcedurePerformer(fhirelement.FHIRElement):
    """ The people who performed the procedure.
    
    Limited to 'real' people rather than equipment.
    """
    
    resource_name = "ProcedurePerformer"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actor = None
        """ The reference to the practitioner.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.role = None
        """ The role the actor was in.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProcedurePerformer, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False),
            ("role", "role", codeableconcept.CodeableConcept, False),
        ])
        return js

