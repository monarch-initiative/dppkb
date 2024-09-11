# Auto generated from dppkb.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-09-10T15:16:51
# Schema: dppkb
#
# id: https://w3id.org/dppkb
# description: Disease Pathophysiology Knowledge Base Schema
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Float, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
DPPKB = CurieNamespace('dppkb', 'https://w3id.org/dppkb/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DPPKB


# Types
class PMID(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PMID"
    type_model_uri = DPPKB.PMID


class FrequencyQuantity(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "FrequencyQuantity"
    type_model_uri = DPPKB.FrequencyQuantity


# Class references
class SubtypeName(extended_str):
    pass


class EpidemiologyInfoName(extended_str):
    pass


class PathophysiologyName(extended_str):
    pass


class PhenotypeName(extended_str):
    pass


class BiochemicalName(extended_str):
    pass


class GeneticName(extended_str):
    pass


class EnvironmentalName(extended_str):
    pass


class DiseaseName(extended_str):
    pass


class TreatmentName(extended_str):
    pass


class InfectiousAgentName(extended_str):
    pass


class TransmissionName(extended_str):
    pass


class AssayName(extended_str):
    pass


class DiagnosisName(extended_str):
    pass


class InheritanceName(extended_str):
    pass


class VariantName(extended_str):
    pass


class MechanismName(extended_str):
    pass


class ModelingConsiderationName(extended_str):
    pass


Any = Any

@dataclass
class Subtype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Subtype"]
    class_class_curie: ClassVar[str] = "dppkb:Subtype"
    class_name: ClassVar[str] = "Subtype"
    class_model_uri: ClassVar[URIRef] = DPPKB.Subtype

    name: Union[str, SubtypeName] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, "EvidenceItem"], List[Union[dict, "EvidenceItem"]]]] = empty_list()
    review_notes: Optional[str] = None
    locations: Optional[Union[Union[str, "AnatomicalEntityTerm"], List[Union[str, "AnatomicalEntityTerm"]]]] = empty_list()
    geography: Optional[Union[Union[str, "GeographyTerm"], List[Union[str, "GeographyTerm"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SubtypeName):
            self.name = SubtypeName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        super().__post_init__(**kwargs)


@dataclass
class EvidenceItem(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["EvidenceItem"]
    class_class_curie: ClassVar[str] = "dppkb:EvidenceItem"
    class_name: ClassVar[str] = "EvidenceItem"
    class_model_uri: ClassVar[URIRef] = DPPKB.EvidenceItem

    reference: Optional[Union[str, PMID]] = None
    supports: Optional[Union[str, "EvidenceItemSupportEnum"]] = None
    snippet: Optional[str] = None
    explanation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.reference is not None and not isinstance(self.reference, PMID):
            self.reference = PMID(self.reference)

        if self.supports is not None and not isinstance(self.supports, EvidenceItemSupportEnum):
            self.supports = EvidenceItemSupportEnum(self.supports)

        if self.snippet is not None and not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        super().__post_init__(**kwargs)


@dataclass
class Prevalence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Prevalence"]
    class_class_curie: ClassVar[str] = "dppkb:Prevalence"
    class_name: ClassVar[str] = "Prevalence"
    class_model_uri: ClassVar[URIRef] = DPPKB.Prevalence

    subtype: Optional[str] = None
    population: Optional[str] = None
    percentage: Optional[Union[dict, Any]] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass
class ProgressionInfo(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["ProgressionInfo"]
    class_class_curie: ClassVar[str] = "dppkb:ProgressionInfo"
    class_name: ClassVar[str] = "ProgressionInfo"
    class_model_uri: ClassVar[URIRef] = DPPKB.ProgressionInfo

    phase: Optional[Union[str, "PhaseTerm"]] = None
    subtype: Optional[str] = None
    age_range: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    incubation_days: Optional[str] = None
    review_notes: Optional[str] = None
    incubation_years: Optional[str] = None
    notes: Optional[str] = None
    duration_days: Optional[str] = None
    duration: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if self.age_range is not None and not isinstance(self.age_range, str):
            self.age_range = str(self.age_range)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.incubation_days is not None and not isinstance(self.incubation_days, str):
            self.incubation_days = str(self.incubation_days)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.incubation_years is not None and not isinstance(self.incubation_years, str):
            self.incubation_years = str(self.incubation_years)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.duration_days is not None and not isinstance(self.duration_days, str):
            self.duration_days = str(self.duration_days)

        if self.duration is not None and not isinstance(self.duration, str):
            self.duration = str(self.duration)

        super().__post_init__(**kwargs)


@dataclass
class EpidemiologyInfo(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["EpidemiologyInfo"]
    class_class_curie: ClassVar[str] = "dppkb:EpidemiologyInfo"
    class_name: ClassVar[str] = "EpidemiologyInfo"
    class_model_uri: ClassVar[URIRef] = DPPKB.EpidemiologyInfo

    name: Union[str, EpidemiologyInfoName] = None
    description: Optional[str] = None
    minimum_value: Optional[float] = None
    maximum_value: Optional[float] = None
    mean_range: Optional[str] = None
    notes: Optional[str] = None
    factors: Optional[Union[str, List[str]]] = empty_list()
    unit: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, EpidemiologyInfoName):
            self.name = EpidemiologyInfoName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.minimum_value is not None and not isinstance(self.minimum_value, float):
            self.minimum_value = float(self.minimum_value)

        if self.maximum_value is not None and not isinstance(self.maximum_value, float):
            self.maximum_value = float(self.maximum_value)

        if self.mean_range is not None and not isinstance(self.mean_range, str):
            self.mean_range = str(self.mean_range)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.factors, list):
            self.factors = [self.factors] if self.factors is not None else []
        self.factors = [v if isinstance(v, str) else str(v) for v in self.factors]

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass
class Pathophysiology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Pathophysiology"]
    class_class_curie: ClassVar[str] = "dppkb:Pathophysiology"
    class_name: ClassVar[str] = "Pathophysiology"
    class_model_uri: ClassVar[URIRef] = DPPKB.Pathophysiology

    name: Union[str, PathophysiologyName] = None
    description: Optional[str] = None
    cell_types: Optional[Union[Union[str, "CellTypeTerm"], List[Union[str, "CellTypeTerm"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    biological_processes: Optional[Union[Union[str, "BiologicalProcessTerm"], List[Union[str, "BiologicalProcessTerm"]]]] = empty_list()
    locations: Optional[Union[Union[str, "AnatomicalEntityTerm"], List[Union[str, "AnatomicalEntityTerm"]]]] = empty_list()
    examples: Optional[Union[str, List[str]]] = empty_list()
    role: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    consequence: Optional[str] = None
    gene: Optional[Union[str, "GeneTerm"]] = None
    pathways: Optional[Union[Union[str, "BiologicalProcessTerm"], List[Union[str, "BiologicalProcessTerm"]]]] = empty_list()
    downstream: Optional[Union[str, List[str]]] = empty_list()
    genes: Optional[Union[Union[str, "GeneTerm"], List[Union[str, "GeneTerm"]]]] = empty_list()
    subtypes: Optional[Union[str, List[str]]] = empty_list()
    cellular_components: Optional[Union[Union[str, "CellularComponentTerm"], List[Union[str, "CellularComponentTerm"]]]] = empty_list()
    chemical_entities: Optional[Union[Union[str, "ChemicalEntityTerm"], List[Union[str, "ChemicalEntityTerm"]]]] = empty_list()
    triggers: Optional[Union[Union[str, "TriggerTerm"], List[Union[str, "TriggerTerm"]]]] = empty_list()
    assays: Optional[Union[Union[str, "AssayTerm"], List[Union[str, "AssayTerm"]]]] = empty_list()
    mechanisms: Optional[Union[str, List[str]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, PathophysiologyName):
            self.name = PathophysiologyName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.consequence is not None and not isinstance(self.consequence, str):
            self.consequence = str(self.consequence)

        if not isinstance(self.downstream, list):
            self.downstream = [self.downstream] if self.downstream is not None else []
        self.downstream = [v if isinstance(v, str) else str(v) for v in self.downstream]

        if not isinstance(self.subtypes, list):
            self.subtypes = [self.subtypes] if self.subtypes is not None else []
        self.subtypes = [v if isinstance(v, str) else str(v) for v in self.subtypes]

        if not isinstance(self.mechanisms, list):
            self.mechanisms = [self.mechanisms] if self.mechanisms is not None else []
        self.mechanisms = [v if isinstance(v, str) else str(v) for v in self.mechanisms]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass
class Phenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Phenotype"]
    class_class_curie: ClassVar[str] = "dppkb:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = DPPKB.Phenotype

    name: Union[str, PhenotypeName] = None
    category: Optional[str] = None
    frequency: Optional[Union[dict, Any]] = None
    diagnostic: Optional[Union[bool, Bool]] = None
    sequelae: Optional[Union[str, List[str]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    context: Optional[str] = None
    review_notes: Optional[str] = None
    severity: Optional[str] = None
    notes: Optional[str] = None
    subtype: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, PhenotypeName):
            self.name = PhenotypeName(self.name)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if self.diagnostic is not None and not isinstance(self.diagnostic, Bool):
            self.diagnostic = Bool(self.diagnostic)

        if not isinstance(self.sequelae, list):
            self.sequelae = [self.sequelae] if self.sequelae is not None else []
        self.sequelae = [v if isinstance(v, str) else str(v) for v in self.sequelae]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        super().__post_init__(**kwargs)


@dataclass
class Biochemical(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Biochemical"]
    class_class_curie: ClassVar[str] = "dppkb:Biochemical"
    class_name: ClassVar[str] = "Biochemical"
    class_model_uri: ClassVar[URIRef] = DPPKB.Biochemical

    name: Union[str, BiochemicalName] = None
    presence: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    specificity: Optional[str] = None
    frequency: Optional[Union[dict, Any]] = None
    notes: Optional[str] = None
    context: Optional[str] = None
    subtype: Optional[str] = None
    cell_types: Optional[Union[Union[str, "CellTypeTerm"], List[Union[str, "CellTypeTerm"]]]] = empty_list()
    assays: Optional[Union[Union[str, "AssayTerm"], List[Union[str, "AssayTerm"]]]] = empty_list()
    synonyms: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BiochemicalName):
            self.name = BiochemicalName(self.name)

        if self.presence is not None and not isinstance(self.presence, str):
            self.presence = str(self.presence)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.specificity is not None and not isinstance(self.specificity, str):
            self.specificity = str(self.specificity)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        super().__post_init__(**kwargs)


@dataclass
class Genetic(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Genetic"]
    class_class_curie: ClassVar[str] = "dppkb:Genetic"
    class_name: ClassVar[str] = "Genetic"
    class_model_uri: ClassVar[URIRef] = DPPKB.Genetic

    name: Union[str, GeneticName] = None
    presence: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    association: Optional[str] = None
    review_notes: Optional[str] = None
    subtype: Optional[str] = None
    frequency: Optional[Union[dict, Any]] = None
    inheritance: Optional[Union[Dict[Union[str, InheritanceName], Union[dict, "Inheritance"]], List[Union[dict, "Inheritance"]]]] = empty_dict()
    variants: Optional[Union[Dict[Union[str, VariantName], Union[dict, "Variant"]], List[Union[dict, "Variant"]]]] = empty_dict()
    features: Optional[str] = None
    notes: Optional[str] = None
    examples: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, GeneticName):
            self.name = GeneticName(self.name)

        if self.presence is not None and not isinstance(self.presence, str):
            self.presence = str(self.presence)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.association is not None and not isinstance(self.association, str):
            self.association = str(self.association)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        self._normalize_inlined_as_list(slot_name="inheritance", slot_type=Inheritance, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="variants", slot_type=Variant, key_name="name", keyed=True)

        if self.features is not None and not isinstance(self.features, str):
            self.features = str(self.features)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        super().__post_init__(**kwargs)


@dataclass
class Environmental(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Environmental"]
    class_class_curie: ClassVar[str] = "dppkb:Environmental"
    class_name: ClassVar[str] = "Environmental"
    class_model_uri: ClassVar[URIRef] = DPPKB.Environmental

    name: Union[str, EnvironmentalName] = None
    presence: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    description: Optional[str] = None
    chemicals: Optional[Union[str, List[str]]] = empty_list()
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    effect: Optional[str] = None
    examples: Optional[Union[str, List[str]]] = empty_list()
    review_notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, EnvironmentalName):
            self.name = EnvironmentalName(self.name)

        if self.presence is not None and not isinstance(self.presence, str):
            self.presence = str(self.presence)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.chemicals, list):
            self.chemicals = [self.chemicals] if self.chemicals is not None else []
        self.chemicals = [v if isinstance(v, str) else str(v) for v in self.chemicals]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.effect is not None and not isinstance(self.effect, str):
            self.effect = str(self.effect)

        if not isinstance(self.examples, list):
            self.examples = [self.examples] if self.examples is not None else []
        self.examples = [v if isinstance(v, str) else str(v) for v in self.examples]

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        super().__post_init__(**kwargs)


@dataclass
class Disease(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Disease"]
    class_class_curie: ClassVar[str] = "dppkb:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = DPPKB.Disease

    name: Union[str, DiseaseName] = None
    description: Optional[str] = None
    category: Optional[str] = None
    parents: Optional[Union[str, List[str]]] = empty_list()
    has_subtypes: Optional[Union[Dict[Union[str, SubtypeName], Union[dict, Subtype]], List[Union[dict, Subtype]]]] = empty_dict()
    prevalence: Optional[Union[Union[dict, Prevalence], List[Union[dict, Prevalence]]]] = empty_list()
    progression: Optional[Union[Union[dict, ProgressionInfo], List[Union[dict, ProgressionInfo]]]] = empty_list()
    pathophysiology: Optional[Union[Dict[Union[str, PathophysiologyName], Union[dict, Pathophysiology]], List[Union[dict, Pathophysiology]]]] = empty_dict()
    phenotypes: Optional[Union[Dict[Union[str, PhenotypeName], Union[dict, Phenotype]], List[Union[dict, Phenotype]]]] = empty_dict()
    biochemical: Optional[Union[Dict[Union[str, BiochemicalName], Union[dict, Biochemical]], List[Union[dict, Biochemical]]]] = empty_dict()
    genetic: Optional[Union[Dict[Union[str, GeneticName], Union[dict, Genetic]], List[Union[dict, Genetic]]]] = empty_dict()
    environmental: Optional[Union[Dict[Union[str, EnvironmentalName], Union[dict, Environmental]], List[Union[dict, Environmental]]]] = empty_dict()
    treatments: Optional[Union[Dict[Union[str, TreatmentName], Union[dict, "Treatment"]], List[Union[dict, "Treatment"]]]] = empty_dict()
    categories: Optional[Union[str, List[str]]] = empty_list()
    infectious_agent: Optional[Union[Dict[Union[str, InfectiousAgentName], Union[dict, "InfectiousAgent"]], List[Union[dict, "InfectiousAgent"]]]] = empty_dict()
    transmission: Optional[Union[Dict[Union[str, TransmissionName], Union[dict, "Transmission"]], List[Union[dict, "Transmission"]]]] = empty_dict()
    modeling_considerations: Optional[Union[Dict[Union[str, ModelingConsiderationName], Union[dict, "ModelingConsideration"]], List[Union[dict, "ModelingConsideration"]]]] = empty_dict()
    epidemiology: Optional[Union[Dict[Union[str, EpidemiologyInfoName], Union[dict, EpidemiologyInfo]], List[Union[dict, EpidemiologyInfo]]]] = empty_dict()
    diagnosis: Optional[Union[Dict[Union[str, DiagnosisName], Union[dict, "Diagnosis"]], List[Union[dict, "Diagnosis"]]]] = empty_dict()
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    inheritance: Optional[Union[Dict[Union[str, InheritanceName], Union[dict, "Inheritance"]], List[Union[dict, "Inheritance"]]]] = empty_dict()
    animal_models: Optional[Union[Union[dict, "AnimalModel"], List[Union[dict, "AnimalModel"]]]] = empty_list()
    notes: Optional[str] = None
    review_notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DiseaseName):
            self.name = DiseaseName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if not isinstance(self.parents, list):
            self.parents = [self.parents] if self.parents is not None else []
        self.parents = [v if isinstance(v, str) else str(v) for v in self.parents]

        self._normalize_inlined_as_list(slot_name="has_subtypes", slot_type=Subtype, key_name="name", keyed=True)

        if not isinstance(self.prevalence, list):
            self.prevalence = [self.prevalence] if self.prevalence is not None else []
        self.prevalence = [v if isinstance(v, Prevalence) else Prevalence(**as_dict(v)) for v in self.prevalence]

        if not isinstance(self.progression, list):
            self.progression = [self.progression] if self.progression is not None else []
        self.progression = [v if isinstance(v, ProgressionInfo) else ProgressionInfo(**as_dict(v)) for v in self.progression]

        self._normalize_inlined_as_list(slot_name="pathophysiology", slot_type=Pathophysiology, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="phenotypes", slot_type=Phenotype, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="biochemical", slot_type=Biochemical, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="genetic", slot_type=Genetic, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="environmental", slot_type=Environmental, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="treatments", slot_type=Treatment, key_name="name", keyed=True)

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, str) else str(v) for v in self.categories]

        self._normalize_inlined_as_list(slot_name="infectious_agent", slot_type=InfectiousAgent, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="transmission", slot_type=Transmission, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="modeling_considerations", slot_type=ModelingConsideration, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="epidemiology", slot_type=EpidemiologyInfo, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="diagnosis", slot_type=Diagnosis, key_name="name", keyed=True)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        self._normalize_inlined_as_list(slot_name="inheritance", slot_type=Inheritance, key_name="name", keyed=True)

        if not isinstance(self.animal_models, list):
            self.animal_models = [self.animal_models] if self.animal_models is not None else []
        self.animal_models = [v if isinstance(v, AnimalModel) else AnimalModel(**as_dict(v)) for v in self.animal_models]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        super().__post_init__(**kwargs)


@dataclass
class AnimalModel(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["AnimalModel"]
    class_class_curie: ClassVar[str] = "dppkb:AnimalModel"
    class_name: ClassVar[str] = "AnimalModel"
    class_model_uri: ClassVar[URIRef] = DPPKB.AnimalModel

    species: Optional[str] = None
    genotype: Optional[str] = None
    background: Optional[str] = None
    genes: Optional[Union[Union[str, "GeneTerm"], List[Union[str, "GeneTerm"]]]] = empty_list()
    category: Optional[str] = None
    alleles: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[str] = None
    associated_phenotypes: Optional[Union[str, List[str]]] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.genotype is not None and not isinstance(self.genotype, str):
            self.genotype = str(self.genotype)

        if self.background is not None and not isinstance(self.background, str):
            self.background = str(self.background)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if not isinstance(self.alleles, list):
            self.alleles = [self.alleles] if self.alleles is not None else []
        self.alleles = [v if isinstance(v, str) else str(v) for v in self.alleles]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.associated_phenotypes, list):
            self.associated_phenotypes = [self.associated_phenotypes] if self.associated_phenotypes is not None else []
        self.associated_phenotypes = [v if isinstance(v, str) else str(v) for v in self.associated_phenotypes]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass
class Treatment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Treatment"]
    class_class_curie: ClassVar[str] = "dppkb:Treatment"
    class_name: ClassVar[str] = "Treatment"
    class_model_uri: ClassVar[URIRef] = DPPKB.Treatment

    name: Union[str, TreatmentName] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    context: Optional[str] = None
    review_notes: Optional[str] = None
    role: Optional[str] = None
    mechanism: Optional[Union[Dict[Union[str, MechanismName], Union[dict, "Mechanism"]], List[Union[dict, "Mechanism"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, TreatmentName):
            self.name = TreatmentName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.review_notes is not None and not isinstance(self.review_notes, str):
            self.review_notes = str(self.review_notes)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        self._normalize_inlined_as_list(slot_name="mechanism", slot_type=Mechanism, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class InfectiousAgent(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["InfectiousAgent"]
    class_class_curie: ClassVar[str] = "dppkb:InfectiousAgent"
    class_name: ClassVar[str] = "InfectiousAgent"
    class_model_uri: ClassVar[URIRef] = DPPKB.InfectiousAgent

    name: Union[str, InfectiousAgentName] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    description: Optional[str] = None
    has_subtypes: Optional[Union[Dict[Union[str, SubtypeName], Union[dict, Subtype]], List[Union[dict, Subtype]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InfectiousAgentName):
            self.name = InfectiousAgentName(self.name)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="has_subtypes", slot_type=Subtype, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Transmission(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Transmission"]
    class_class_curie: ClassVar[str] = "dppkb:Transmission"
    class_name: ClassVar[str] = "Transmission"
    class_model_uri: ClassVar[URIRef] = DPPKB.Transmission

    name: Union[str, TransmissionName] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    effect: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, TransmissionName):
            self.name = TransmissionName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.effect is not None and not isinstance(self.effect, str):
            self.effect = str(self.effect)

        super().__post_init__(**kwargs)


@dataclass
class Assay(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Assay"]
    class_class_curie: ClassVar[str] = "dppkb:Assay"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = DPPKB.Assay

    name: Union[str, AssayName] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, AssayName):
            self.name = AssayName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Diagnosis(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Diagnosis"]
    class_class_curie: ClassVar[str] = "dppkb:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = DPPKB.Diagnosis

    name: Union[str, DiagnosisName] = None
    presence: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    notes: Optional[str] = None
    results: Optional[str] = None
    markers: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DiagnosisName):
            self.name = DiagnosisName(self.name)

        if self.presence is not None and not isinstance(self.presence, str):
            self.presence = str(self.presence)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.results is not None and not isinstance(self.results, str):
            self.results = str(self.results)

        if self.markers is not None and not isinstance(self.markers, str):
            self.markers = str(self.markers)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Inheritance(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Inheritance"]
    class_class_curie: ClassVar[str] = "dppkb:Inheritance"
    class_name: ClassVar[str] = "Inheritance"
    class_model_uri: ClassVar[URIRef] = DPPKB.Inheritance

    name: Union[str, InheritanceName] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InheritanceName):
            self.name = InheritanceName(self.name)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Variant(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Variant"]
    class_class_curie: ClassVar[str] = "dppkb:Variant"
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = DPPKB.Variant

    name: Union[str, VariantName] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, VariantName):
            self.name = VariantName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Mechanism(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["Mechanism"]
    class_class_curie: ClassVar[str] = "dppkb:Mechanism"
    class_name: ClassVar[str] = "Mechanism"
    class_model_uri: ClassVar[URIRef] = DPPKB.Mechanism

    name: Union[str, MechanismName] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, MechanismName):
            self.name = MechanismName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class ModelingConsideration(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["ModelingConsideration"]
    class_class_curie: ClassVar[str] = "dppkb:ModelingConsideration"
    class_name: ClassVar[str] = "ModelingConsideration"
    class_model_uri: ClassVar[URIRef] = DPPKB.ModelingConsideration

    name: Union[str, ModelingConsiderationName] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ModelingConsiderationName):
            self.name = ModelingConsiderationName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence]

        super().__post_init__(**kwargs)


@dataclass
class DiseaseCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DPPKB["DiseaseCollection"]
    class_class_curie: ClassVar[str] = "dppkb:DiseaseCollection"
    class_name: ClassVar[str] = "DiseaseCollection"
    class_model_uri: ClassVar[URIRef] = DPPKB.DiseaseCollection

    diseases: Optional[Union[Dict[Union[str, DiseaseName], Union[dict, Disease]], List[Union[dict, Disease]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="diseases", slot_type=Disease, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class EvidenceItemSupportEnum(EnumDefinitionImpl):
    """
    The level of support for an evidence item
    """
    WRONG_STATEMENT = PermissibleValue(
        text="WRONG_STATEMENT",
        description="WRONG_STATEMENT")
    SUPPORT = PermissibleValue(
        text="SUPPORT",
        description="SUPPORT")
    REFUTE = PermissibleValue(
        text="REFUTE",
        description="REFUTE")
    NO_EVIDENCE = PermissibleValue(
        text="NO_EVIDENCE",
        description="NO_EVIDENCE")
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        description="PARTIAL")

    _defn = EnumDefinition(
        name="EvidenceItemSupportEnum",
        description="The level of support for an evidence item",
    )

class FrequencyEnum(EnumDefinitionImpl):
    """
    The frequency of an event or phenomenon
    """
    FREQUENT = PermissibleValue(
        text="FREQUENT",
        description="Common",
        meaning=HP["0040282"])
    OCCASIONAL = PermissibleValue(
        text="OCCASIONAL",
        description="Occasional")
    VERY_FREQUENT = PermissibleValue(
        text="VERY_FREQUENT",
        description="High",
        meaning=HP["0040281"])
    VERY_RARE = PermissibleValue(
        text="VERY_RARE",
        description="Rare",
        meaning=HP["0040284"])
    OBLIGATE = PermissibleValue(
        text="OBLIGATE",
        description="Obligate",
        meaning=HP["0040280"])

    _defn = EnumDefinition(
        name="FrequencyEnum",
        description="The frequency of an event or phenomenon",
    )

class AssayTerm(EnumDefinitionImpl):
    """
    A term representing an assay
    """
    _defn = EnumDefinition(
        name="AssayTerm",
        description="A term representing an assay",
    )

class CellularComponentTerm(EnumDefinitionImpl):
    """
    A term representing a cellular component
    """
    _defn = EnumDefinition(
        name="CellularComponentTerm",
        description="A term representing a cellular component",
    )

class BiologicalProcessTerm(EnumDefinitionImpl):
    """
    A term representing a biological process or pathway
    """
    _defn = EnumDefinition(
        name="BiologicalProcessTerm",
        description="A term representing a biological process or pathway",
    )

class ChemicalEntityTerm(EnumDefinitionImpl):
    """
    A term representing a chemical entity
    """
    _defn = EnumDefinition(
        name="ChemicalEntityTerm",
        description="A term representing a chemical entity",
    )

class PhenotypeTerm(EnumDefinitionImpl):
    """
    A term representing a phenotype
    """
    _defn = EnumDefinition(
        name="PhenotypeTerm",
        description="A term representing a phenotype",
    )

class AnatomicalEntityTerm(EnumDefinitionImpl):
    """
    A term representing an anatomical entity
    """
    _defn = EnumDefinition(
        name="AnatomicalEntityTerm",
        description="A term representing an anatomical entity",
    )

class GeographyTerm(EnumDefinitionImpl):
    """
    A place or location
    """
    _defn = EnumDefinition(
        name="GeographyTerm",
        description="A place or location",
    )

class PhaseTerm(EnumDefinitionImpl):
    """
    A phase or stage
    """
    _defn = EnumDefinition(
        name="PhaseTerm",
        description="A phase or stage",
    )

class TriggerTerm(EnumDefinitionImpl):
    """
    A trigger
    """
    _defn = EnumDefinition(
        name="TriggerTerm",
        description="A trigger",
    )

class GeneTerm(EnumDefinitionImpl):
    """
    A gene
    """
    _defn = EnumDefinition(
        name="GeneTerm",
        description="A gene",
    )

class CellTypeTerm(EnumDefinitionImpl):
    """
    A cell type
    """
    _defn = EnumDefinition(
        name="CellTypeTerm",
        description="A cell type",
    )

class DiseaseTerm(EnumDefinitionImpl):
    """
    A disease or medical condition
    """
    _defn = EnumDefinition(
        name="DiseaseTerm",
        description="A disease or medical condition",
    )

# Slots
class slots:
    pass

slots.name = Slot(uri=DPPKB.name, name="name", curie=DPPKB.curie('name'),
                   model_uri=DPPKB.name, domain=None, range=URIRef)

slots.description = Slot(uri=DPPKB.description, name="description", curie=DPPKB.curie('description'),
                   model_uri=DPPKB.description, domain=None, range=Optional[str])

slots.evidence = Slot(uri=DPPKB.evidence, name="evidence", curie=DPPKB.curie('evidence'),
                   model_uri=DPPKB.evidence, domain=None, range=Optional[Union[Union[dict, EvidenceItem], List[Union[dict, EvidenceItem]]]])

slots.review_notes = Slot(uri=DPPKB.review_notes, name="review_notes", curie=DPPKB.curie('review_notes'),
                   model_uri=DPPKB.review_notes, domain=None, range=Optional[str])

slots.geography = Slot(uri=DPPKB.geography, name="geography", curie=DPPKB.curie('geography'),
                   model_uri=DPPKB.geography, domain=None, range=Optional[Union[Union[str, "GeographyTerm"], List[Union[str, "GeographyTerm"]]]])

slots.locations = Slot(uri=DPPKB.locations, name="locations", curie=DPPKB.curie('locations'),
                   model_uri=DPPKB.locations, domain=None, range=Optional[Union[Union[str, "AnatomicalEntityTerm"], List[Union[str, "AnatomicalEntityTerm"]]]])

slots.reference = Slot(uri=DPPKB.reference, name="reference", curie=DPPKB.curie('reference'),
                   model_uri=DPPKB.reference, domain=None, range=Optional[Union[str, PMID]])

slots.supports = Slot(uri=DPPKB.supports, name="supports", curie=DPPKB.curie('supports'),
                   model_uri=DPPKB.supports, domain=None, range=Optional[Union[str, "EvidenceItemSupportEnum"]])

slots.snippet = Slot(uri=DPPKB.snippet, name="snippet", curie=DPPKB.curie('snippet'),
                   model_uri=DPPKB.snippet, domain=None, range=Optional[str])

slots.explanation = Slot(uri=DPPKB.explanation, name="explanation", curie=DPPKB.curie('explanation'),
                   model_uri=DPPKB.explanation, domain=None, range=Optional[str])

slots.subtype = Slot(uri=DPPKB.subtype, name="subtype", curie=DPPKB.curie('subtype'),
                   model_uri=DPPKB.subtype, domain=None, range=Optional[str])

slots.population = Slot(uri=DPPKB.population, name="population", curie=DPPKB.curie('population'),
                   model_uri=DPPKB.population, domain=None, range=Optional[str])

slots.percentage = Slot(uri=DPPKB.percentage, name="percentage", curie=DPPKB.curie('percentage'),
                   model_uri=DPPKB.percentage, domain=None, range=Optional[Union[dict, Any]])

slots.phase = Slot(uri=DPPKB.phase, name="phase", curie=DPPKB.curie('phase'),
                   model_uri=DPPKB.phase, domain=None, range=Optional[Union[str, "PhaseTerm"]])

slots.age_range = Slot(uri=DPPKB.age_range, name="age_range", curie=DPPKB.curie('age_range'),
                   model_uri=DPPKB.age_range, domain=None, range=Optional[str])

slots.incubation_days = Slot(uri=DPPKB.incubation_days, name="incubation_days", curie=DPPKB.curie('incubation_days'),
                   model_uri=DPPKB.incubation_days, domain=None, range=Optional[str])

slots.incubation_years = Slot(uri=DPPKB.incubation_years, name="incubation_years", curie=DPPKB.curie('incubation_years'),
                   model_uri=DPPKB.incubation_years, domain=None, range=Optional[str])

slots.notes = Slot(uri=DPPKB.notes, name="notes", curie=DPPKB.curie('notes'),
                   model_uri=DPPKB.notes, domain=None, range=Optional[str])

slots.duration_days = Slot(uri=DPPKB.duration_days, name="duration_days", curie=DPPKB.curie('duration_days'),
                   model_uri=DPPKB.duration_days, domain=None, range=Optional[str])

slots.duration = Slot(uri=DPPKB.duration, name="duration", curie=DPPKB.curie('duration'),
                   model_uri=DPPKB.duration, domain=None, range=Optional[str])

slots.cell_types = Slot(uri=DPPKB.cell_types, name="cell_types", curie=DPPKB.curie('cell_types'),
                   model_uri=DPPKB.cell_types, domain=None, range=Optional[Union[Union[str, "CellTypeTerm"], List[Union[str, "CellTypeTerm"]]]])

slots.biological_processes = Slot(uri=DPPKB.biological_processes, name="biological_processes", curie=DPPKB.curie('biological_processes'),
                   model_uri=DPPKB.biological_processes, domain=None, range=Optional[Union[Union[str, "BiologicalProcessTerm"], List[Union[str, "BiologicalProcessTerm"]]]])

slots.epidemiology = Slot(uri=DPPKB.epidemiology, name="epidemiology", curie=DPPKB.curie('epidemiology'),
                   model_uri=DPPKB.epidemiology, domain=None, range=Optional[Union[Dict[Union[str, EpidemiologyInfoName], Union[dict, EpidemiologyInfo]], List[Union[dict, EpidemiologyInfo]]]])

slots.examples = Slot(uri=DPPKB.examples, name="examples", curie=DPPKB.curie('examples'),
                   model_uri=DPPKB.examples, domain=None, range=Optional[Union[str, List[str]]])

slots.role = Slot(uri=DPPKB.role, name="role", curie=DPPKB.curie('role'),
                   model_uri=DPPKB.role, domain=None, range=Optional[str])

slots.consequence = Slot(uri=DPPKB.consequence, name="consequence", curie=DPPKB.curie('consequence'),
                   model_uri=DPPKB.consequence, domain=None, range=Optional[str])

slots.gene = Slot(uri=DPPKB.gene, name="gene", curie=DPPKB.curie('gene'),
                   model_uri=DPPKB.gene, domain=None, range=Optional[Union[str, "GeneTerm"]])

slots.pathways = Slot(uri=DPPKB.pathways, name="pathways", curie=DPPKB.curie('pathways'),
                   model_uri=DPPKB.pathways, domain=None, range=Optional[Union[Union[str, "BiologicalProcessTerm"], List[Union[str, "BiologicalProcessTerm"]]]])

slots.downstream = Slot(uri=DPPKB.downstream, name="downstream", curie=DPPKB.curie('downstream'),
                   model_uri=DPPKB.downstream, domain=None, range=Optional[Union[str, List[str]]])

slots.genes = Slot(uri=DPPKB.genes, name="genes", curie=DPPKB.curie('genes'),
                   model_uri=DPPKB.genes, domain=None, range=Optional[Union[Union[str, "GeneTerm"], List[Union[str, "GeneTerm"]]]])

slots.subtypes = Slot(uri=DPPKB.subtypes, name="subtypes", curie=DPPKB.curie('subtypes'),
                   model_uri=DPPKB.subtypes, domain=None, range=Optional[Union[str, List[str]]])

slots.has_subtypes = Slot(uri=DPPKB.has_subtypes, name="has_subtypes", curie=DPPKB.curie('has_subtypes'),
                   model_uri=DPPKB.has_subtypes, domain=None, range=Optional[Union[Dict[Union[str, SubtypeName], Union[dict, Subtype]], List[Union[dict, Subtype]]]])

slots.cellular_components = Slot(uri=DPPKB.cellular_components, name="cellular_components", curie=DPPKB.curie('cellular_components'),
                   model_uri=DPPKB.cellular_components, domain=None, range=Optional[Union[Union[str, "CellularComponentTerm"], List[Union[str, "CellularComponentTerm"]]]])

slots.chemical_entities = Slot(uri=DPPKB.chemical_entities, name="chemical_entities", curie=DPPKB.curie('chemical_entities'),
                   model_uri=DPPKB.chemical_entities, domain=None, range=Optional[Union[Union[str, "ChemicalEntityTerm"], List[Union[str, "ChemicalEntityTerm"]]]])

slots.triggers = Slot(uri=DPPKB.triggers, name="triggers", curie=DPPKB.curie('triggers'),
                   model_uri=DPPKB.triggers, domain=None, range=Optional[Union[Union[str, "TriggerTerm"], List[Union[str, "TriggerTerm"]]]])

slots.assays = Slot(uri=DPPKB.assays, name="assays", curie=DPPKB.curie('assays'),
                   model_uri=DPPKB.assays, domain=None, range=Optional[Union[Union[str, "AssayTerm"], List[Union[str, "AssayTerm"]]]])

slots.mechanisms = Slot(uri=DPPKB.mechanisms, name="mechanisms", curie=DPPKB.curie('mechanisms'),
                   model_uri=DPPKB.mechanisms, domain=None, range=Optional[Union[str, List[str]]])

slots.category = Slot(uri=DPPKB.category, name="category", curie=DPPKB.curie('category'),
                   model_uri=DPPKB.category, domain=None, range=Optional[str])

slots.frequency = Slot(uri=DPPKB.frequency, name="frequency", curie=DPPKB.curie('frequency'),
                   model_uri=DPPKB.frequency, domain=None, range=Optional[Union[dict, Any]])

slots.diagnostic = Slot(uri=DPPKB.diagnostic, name="diagnostic", curie=DPPKB.curie('diagnostic'),
                   model_uri=DPPKB.diagnostic, domain=None, range=Optional[Union[bool, Bool]])

slots.sequelae = Slot(uri=DPPKB.sequelae, name="sequelae", curie=DPPKB.curie('sequelae'),
                   model_uri=DPPKB.sequelae, domain=None, range=Optional[Union[str, List[str]]])

slots.context = Slot(uri=DPPKB.context, name="context", curie=DPPKB.curie('context'),
                   model_uri=DPPKB.context, domain=None, range=Optional[str])

slots.severity = Slot(uri=DPPKB.severity, name="severity", curie=DPPKB.curie('severity'),
                   model_uri=DPPKB.severity, domain=None, range=Optional[str])

slots.presence = Slot(uri=DPPKB.presence, name="presence", curie=DPPKB.curie('presence'),
                   model_uri=DPPKB.presence, domain=None, range=Optional[str])

slots.specificity = Slot(uri=DPPKB.specificity, name="specificity", curie=DPPKB.curie('specificity'),
                   model_uri=DPPKB.specificity, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=DPPKB.synonyms, name="synonyms", curie=DPPKB.curie('synonyms'),
                   model_uri=DPPKB.synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.association = Slot(uri=DPPKB.association, name="association", curie=DPPKB.curie('association'),
                   model_uri=DPPKB.association, domain=None, range=Optional[str])

slots.inheritance = Slot(uri=DPPKB.inheritance, name="inheritance", curie=DPPKB.curie('inheritance'),
                   model_uri=DPPKB.inheritance, domain=None, range=Optional[Union[Dict[Union[str, InheritanceName], Union[dict, Inheritance]], List[Union[dict, Inheritance]]]])

slots.variants = Slot(uri=DPPKB.variants, name="variants", curie=DPPKB.curie('variants'),
                   model_uri=DPPKB.variants, domain=None, range=Optional[Union[Dict[Union[str, VariantName], Union[dict, Variant]], List[Union[dict, Variant]]]])

slots.features = Slot(uri=DPPKB.features, name="features", curie=DPPKB.curie('features'),
                   model_uri=DPPKB.features, domain=None, range=Optional[str])

slots.chemicals = Slot(uri=DPPKB.chemicals, name="chemicals", curie=DPPKB.curie('chemicals'),
                   model_uri=DPPKB.chemicals, domain=None, range=Optional[Union[str, List[str]]])

slots.alleles = Slot(uri=DPPKB.alleles, name="alleles", curie=DPPKB.curie('alleles'),
                   model_uri=DPPKB.alleles, domain=None, range=Optional[Union[str, List[str]]])

slots.species = Slot(uri=DPPKB.species, name="species", curie=DPPKB.curie('species'),
                   model_uri=DPPKB.species, domain=None, range=Optional[str])

slots.effect = Slot(uri=DPPKB.effect, name="effect", curie=DPPKB.curie('effect'),
                   model_uri=DPPKB.effect, domain=None, range=Optional[str])

slots.parents = Slot(uri=DPPKB.parents, name="parents", curie=DPPKB.curie('parents'),
                   model_uri=DPPKB.parents, domain=None, range=Optional[Union[str, List[str]]])

slots.prevalence = Slot(uri=DPPKB.prevalence, name="prevalence", curie=DPPKB.curie('prevalence'),
                   model_uri=DPPKB.prevalence, domain=None, range=Optional[Union[Union[dict, Prevalence], List[Union[dict, Prevalence]]]])

slots.progression = Slot(uri=DPPKB.progression, name="progression", curie=DPPKB.curie('progression'),
                   model_uri=DPPKB.progression, domain=None, range=Optional[Union[Union[dict, ProgressionInfo], List[Union[dict, ProgressionInfo]]]])

slots.pathophysiology = Slot(uri=DPPKB.pathophysiology, name="pathophysiology", curie=DPPKB.curie('pathophysiology'),
                   model_uri=DPPKB.pathophysiology, domain=None, range=Optional[Union[Dict[Union[str, PathophysiologyName], Union[dict, Pathophysiology]], List[Union[dict, Pathophysiology]]]])

slots.phenotypes = Slot(uri=DPPKB.phenotypes, name="phenotypes", curie=DPPKB.curie('phenotypes'),
                   model_uri=DPPKB.phenotypes, domain=None, range=Optional[Union[Dict[Union[str, PhenotypeName], Union[dict, Phenotype]], List[Union[dict, Phenotype]]]])

slots.biochemical = Slot(uri=DPPKB.biochemical, name="biochemical", curie=DPPKB.curie('biochemical'),
                   model_uri=DPPKB.biochemical, domain=None, range=Optional[Union[Dict[Union[str, BiochemicalName], Union[dict, Biochemical]], List[Union[dict, Biochemical]]]])

slots.genetic = Slot(uri=DPPKB.genetic, name="genetic", curie=DPPKB.curie('genetic'),
                   model_uri=DPPKB.genetic, domain=None, range=Optional[Union[Dict[Union[str, GeneticName], Union[dict, Genetic]], List[Union[dict, Genetic]]]])

slots.environmental = Slot(uri=DPPKB.environmental, name="environmental", curie=DPPKB.curie('environmental'),
                   model_uri=DPPKB.environmental, domain=None, range=Optional[Union[Dict[Union[str, EnvironmentalName], Union[dict, Environmental]], List[Union[dict, Environmental]]]])

slots.treatments = Slot(uri=DPPKB.treatments, name="treatments", curie=DPPKB.curie('treatments'),
                   model_uri=DPPKB.treatments, domain=None, range=Optional[Union[Dict[Union[str, TreatmentName], Union[dict, Treatment]], List[Union[dict, Treatment]]]])

slots.categories = Slot(uri=DPPKB.categories, name="categories", curie=DPPKB.curie('categories'),
                   model_uri=DPPKB.categories, domain=None, range=Optional[Union[str, List[str]]])

slots.infectious_agent = Slot(uri=DPPKB.infectious_agent, name="infectious_agent", curie=DPPKB.curie('infectious_agent'),
                   model_uri=DPPKB.infectious_agent, domain=None, range=Optional[Union[Dict[Union[str, InfectiousAgentName], Union[dict, InfectiousAgent]], List[Union[dict, InfectiousAgent]]]])

slots.transmission = Slot(uri=DPPKB.transmission, name="transmission", curie=DPPKB.curie('transmission'),
                   model_uri=DPPKB.transmission, domain=None, range=Optional[Union[Dict[Union[str, TransmissionName], Union[dict, Transmission]], List[Union[dict, Transmission]]]])

slots.diagnosis = Slot(uri=DPPKB.diagnosis, name="diagnosis", curie=DPPKB.curie('diagnosis'),
                   model_uri=DPPKB.diagnosis, domain=None, range=Optional[Union[Dict[Union[str, DiagnosisName], Union[dict, Diagnosis]], List[Union[dict, Diagnosis]]]])

slots.modeling_considerations = Slot(uri=DPPKB.modeling_considerations, name="modeling_considerations", curie=DPPKB.curie('modeling_considerations'),
                   model_uri=DPPKB.modeling_considerations, domain=None, range=Optional[Union[Dict[Union[str, ModelingConsiderationName], Union[dict, ModelingConsideration]], List[Union[dict, ModelingConsideration]]]])

slots.mechanism = Slot(uri=DPPKB.mechanism, name="mechanism", curie=DPPKB.curie('mechanism'),
                   model_uri=DPPKB.mechanism, domain=None, range=Optional[Union[Dict[Union[str, MechanismName], Union[dict, Mechanism]], List[Union[dict, Mechanism]]]])

slots.results = Slot(uri=DPPKB.results, name="results", curie=DPPKB.curie('results'),
                   model_uri=DPPKB.results, domain=None, range=Optional[str])

slots.markers = Slot(uri=DPPKB.markers, name="markers", curie=DPPKB.curie('markers'),
                   model_uri=DPPKB.markers, domain=None, range=Optional[str])

slots.diseases = Slot(uri=DPPKB.diseases, name="diseases", curie=DPPKB.curie('diseases'),
                   model_uri=DPPKB.diseases, domain=None, range=Optional[Union[Dict[Union[str, DiseaseName], Union[dict, Disease]], List[Union[dict, Disease]]]])

slots.animal_models = Slot(uri=DPPKB.animal_models, name="animal_models", curie=DPPKB.curie('animal_models'),
                   model_uri=DPPKB.animal_models, domain=None, range=Optional[Union[Union[dict, AnimalModel], List[Union[dict, AnimalModel]]]])

slots.genotype = Slot(uri=DPPKB.genotype, name="genotype", curie=DPPKB.curie('genotype'),
                   model_uri=DPPKB.genotype, domain=None, range=Optional[str])

slots.background = Slot(uri=DPPKB.background, name="background", curie=DPPKB.curie('background'),
                   model_uri=DPPKB.background, domain=None, range=Optional[str])

slots.associated_phenotypes = Slot(uri=DPPKB.associated_phenotypes, name="associated_phenotypes", curie=DPPKB.curie('associated_phenotypes'),
                   model_uri=DPPKB.associated_phenotypes, domain=None, range=Optional[Union[str, List[str]]])

slots.minimum_value = Slot(uri=DPPKB.minimum_value, name="minimum_value", curie=DPPKB.curie('minimum_value'),
                   model_uri=DPPKB.minimum_value, domain=None, range=Optional[float])

slots.maximum_value = Slot(uri=DPPKB.maximum_value, name="maximum_value", curie=DPPKB.curie('maximum_value'),
                   model_uri=DPPKB.maximum_value, domain=None, range=Optional[float])

slots.mean_range = Slot(uri=DPPKB.mean_range, name="mean_range", curie=DPPKB.curie('mean_range'),
                   model_uri=DPPKB.mean_range, domain=None, range=Optional[str])

slots.factors = Slot(uri=DPPKB.factors, name="factors", curie=DPPKB.curie('factors'),
                   model_uri=DPPKB.factors, domain=None, range=Optional[Union[str, List[str]]])

slots.unit = Slot(uri=DPPKB.unit, name="unit", curie=DPPKB.curie('unit'),
                   model_uri=DPPKB.unit, domain=None, range=Optional[str])