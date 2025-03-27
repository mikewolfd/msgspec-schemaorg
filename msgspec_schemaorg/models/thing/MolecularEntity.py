from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.Grant import Grant
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.thing.BioChemEntity import BioChemEntity
    from msgspec_schemaorg.models.thing.Gene import Gene
    from msgspec_schemaorg.models.thing.MedicalCondition import MedicalCondition
    from msgspec_schemaorg.models.thing.Taxon import Taxon


class MolecularEntity(Struct, frozen=True):
    """Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity."""
    name: str | None = None
    mainEntityOfPage: str | 'CreativeWork' | None = None
    url: str | None = None
    disambiguatingDescription: str | None = None
    identifier: str | 'PropertyValue' | str | None = None
    description: str | 'TextObject' | None = None
    subjectOf: 'Event' | 'CreativeWork' | None = None
    alternateName: str | None = None
    additionalType: str | str | None = None
    potentialAction: 'Action' | None = None
    sameAs: str | None = None
    image: 'ImageObject' | str | None = None
    bioChemSimilarity: 'BioChemEntity' | None = None
    hasRepresentation: 'PropertyValue' | str | str | None = None
    hasBioChemEntityPart: 'BioChemEntity' | None = None
    taxonomicRange: str | 'DefinedTerm' | str | 'Taxon' | None = None
    funding: 'Grant' | None = None
    isEncodedByBioChemEntity: 'Gene' | None = None
    isInvolvedInBiologicalProcess: 'PropertyValue' | 'DefinedTerm' | str | None = None
    associatedDisease: 'MedicalCondition' | str | 'PropertyValue' | None = None
    bioChemInteraction: 'BioChemEntity' | None = None
    isLocatedInSubcellularLocation: 'PropertyValue' | 'DefinedTerm' | str | None = None
    hasMolecularFunction: 'PropertyValue' | 'DefinedTerm' | str | None = None
    biologicalRole: 'DefinedTerm' | None = None
    isPartOfBioChemEntity: 'BioChemEntity' | None = None
    molecularWeight: 'QuantitativeValue' | str | None = None
    monoisotopicMolecularWeight: str | 'QuantitativeValue' | None = None
    potentialUse: 'DefinedTerm' | None = None
    inChI: str | None = None
    iupacName: str | None = None
    molecularFormula: str | None = None
    inChIKey: str | None = None
    smiles: str | None = None
    chemicalRole: 'DefinedTerm' | None = None