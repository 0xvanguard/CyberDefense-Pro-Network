/**
 * MedScan Knowledge Base
 * Verified medical claims from WHO, CDC, PubMed, NIH
 * Each entry: { pattern, verdict, explanation, sources, category }
 * 
 * verdict: "false" | "misleading" | "unverified" | "true"
 */

const MEDICAL_KNOWLEDGE_BASE = [
  // ========== VACCINES ==========
  {
    id: "VAX-001",
    patterns: [
      /vaci[ua]n[ea]s?\s+causan?\s+autismo/i,
      /autismo\s+por\s+vacunas/i,
      /vacunas\s+y\s+autismo/i,
      /vacuna\s+produc[ei]\s+autismo/i
    ],
    verdict: "false",
    confidence: 0.99,
    explanation: "Múltiples estudios con millones de participantes demuestran que NO existe relación entre vacunas y autismo. El estudio original de Wakefield (1998) fue retractado por fraude.",
    sources: [
      { name: "CDC", url: "https://www.cdc.gov/vaccinesafety/concerns/autism.html" },
      { name: "OMS", url: "https://www.who.int/news-room/questions-and-answers/item/vaccines-and-immunization-what-is-vaccination" },
      { name: "The Lancet", url: "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext" }
    ],
    category: "vaccines",
    severity: "high"
  },
  {
    id: "VAX-002",
    patterns: [
      /vacunas?\s+contienen?\s+microchips?/i,
      /chip\s+en\s+la\s+vacuna/i,
      /vacuna\s+de\s+5g/i,
      /vacuna\s+control/i
    ],
    verdict: "false",
    confidence: 0.99,
    explanation: "Las vacunas NO contienen microchips, rastreadores ni tecnología 5G. Sus ingredientes son públicos y verificados por agencias regulatorias de múltiples países.",
    sources: [
      { name: "FDA - Ingredientes", url: "https://www.fda.gov/emergency-preparedness-and-response/coronavirus-disease-2019-covid-19/covid-19-vaccines" },
      { name: "EMA", url: "https://www.ema.europa.eu/en/human-regulatory-overview/public-health-threats/coronavirus-disease-covid-19/covid-19-vaccines" }
    ],
    category: "vaccines",
    severity: "high"
  },
  {
    id: "VAX-003",
    patterns: [
      /mejor\s+natur[oa]l[ea]?\s+que\s+vacunar/i,
      /inmunidad\s+natural\s+mejor\s+que\s+vacuna/i,
      /vacuna\s+no\s+es\s+necesaria/i
    ],
    verdict: "misleading",
    confidence: 0.85,
    explanation: "La inmunidad natural existe pero el costo puede ser hospitalización, complicaciones graves o muerte. Las vacunas ofrecen protección con riesgo significativamente menor.",
    sources: [
      { name: "CDC - Natural Immunity", url: "https://www.cdc.gov/coronavirus/2019-ncov/science/science-briefs/vaccine-induced-immunity.html" },
      { name: "Nature Medicine", url: "https://www.nature.com/articles/s41591-022-02051-3" }
    ],
    category: "vaccines",
    severity: "medium"
  },

  // ========== CANCER ==========
  {
    id: "CAN-001",
    patterns: [
      /bicarbonato\s+cura\s+cancer/i,
      /bicarbonato\s+de\s+sodio\s+y\s+cancer/i,
      /alcaliniza[rn]?\s+el\s+cuerpo\s+y\s+cancer/i,
      /ph\s+alcalino\s+cura/i
    ],
    verdict: "false",
    confidence: 0.98,
    explanation: "No existe evidencia científica de que el bicarbonato de sodio cure el cáncer. El cáncer no se 'alcaliniza'. Los tumores tienen su propio microambiente ácido que no se altera con dieta.",
    sources: [
      { name: "American Cancer Society", url: "https://www.cancer.org/treatment/treatments-and-side-effects/complementary-and-alternative-medicine/dietary-supplements.html" },
      { name: "NCI", url: "https://www.cancer.gov/about-cancer/treatment/cam/hp/baking-soda-pdq" }
    ],
    category: "cancer",
    severity: "critical"
  },
  {
    id: "CAN-002",
    patterns: [
      /quimioterapia\s+es\s+peor/i,
      /quimio\s+mata\s+más/i,
      /quimioterapia\s+no\s+funciona/i,
      /no\s+hagas\s+quimio/i
    ],
    verdict: "false",
    confidence: 0.95,
    explanation: "La quimioterapia ha salvado millones de vidas. Para muchos cánceres, es el tratamiento estándar con mayor tasa de supervivencia. Suspenderla por consejo no médico puede ser fatal.",
    sources: [
      { name: "NCI - Chemotherapy", url: "https://www.cancer.gov/about-cancer/treatment/types/chemotherapy" },
      { name: "Cochrane Reviews", url: "https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD012244.pub2/full" }
    ],
    category: "cancer",
    severity: "critical"
  },
  {
    id: "CAN-003",
    patterns: [
      /azúcar\s+alimenta\s+cancer/i,
      /azúcar\s+causa\s+cancer/i,
      /eliminar\s+azúcar\s+cura\s+cancer/i,
      /cancer\s+se\s+alimenta\s+de\s+azúcar/i
    ],
    verdict: "misleading",
    confidence: 0.80,
    explanation: "Las células cancerosas usan glucosa, pero TODAS las células del cuerpo usan glucosa. Reducir azúcar no 'alimenta' ni 'desalimenta' el cáncer directamente. La dieta sola no cura el cáncer.",
    sources: [
      { name: "Cancer Research UK", url: "https://www.cancerresearchuk.org/about-cancer/causes-and-prevention/diet-and-cancer/does-sugar-cause-cancer" },
      { name: "MD Anderson", url: "https://www.mdanderson.org/cancerwise/does-sugar-feed-cancer.h00-159385478.html" }
    ],
    category: "cancer",
    severity: "high"
  },

  // ========== COVID-19 ==========
  {
    id: "COVID-001",
    patterns: [
      /ivermectina\s+cure\s+covid/i,
      /ivermectina\s+para\s+covid/i,
      /ivermectina\s+previene\s+covid/i
    ],
    verdict: "misleading",
    confidence: 0.88,
    explanation: "La ivermectina es un antiparasitario. Estudios iniciales prometedores NO se replicaron en ensayos controlados grandes (WHO SOLIDARITY, TOGETHER). La OMS no la recomienda para COVID.",
    sources: [
      { name: "WHO", url: "https://www.who.int/news/item/31-03-2022-who-downgrades-ivermectin-for-covid-19" },
      { name: "NEJM - TOGETHER Trial", url: "https://www.nejm.org/doi/full/10.1056/NEJMoa2115869" }
    ],
    category: "infectious",
    severity: "high"
  },
  {
    id: "COVID-002",
    patterns: [
      /covid\s+es\s+gripe\s+nada\s+más/i,
      /covid\s+no\s+existe/i,
      /plandemia/i,
      /covid\s+es\s+inventado/i
    ],
    verdict: "false",
    confidence: 0.99,
    explanation: "COVID-19 ha causado más de 7 millones de muertes confirmadas (OMS). El virus SARS-CoV-2 ha sido secuenciado miles de veces por laboratorios independientes en todo el mundo.",
    sources: [
      { name: "WHO Dashboard", url: "https://covid19.who.int/" },
      { name: "GISAID", url: "https://gisaid.org/" }
    ],
    category: "infectious",
    severity: "critical"
  },
  {
    id: "COVID-003",
    patterns: [
      /covid\s+no\s+mata\s+a\s+la\s+gente/i,
      /muertes\s+por\s+covid\s+son\s+falsas/i,
      /inflan\s+las\s+cifras/i
    ],
    verdict: "false",
    confidence: 0.95,
    explanation: "Los excesos de mortalidad (muertes totales vs esperadas) confirman las cifras de COVID. Países independientes con diferentes gobiernos reportaron patrones similares.",
    sources: [
      { name: "The Economist - Excess Deaths", url: "https://www.economist.com/graphic-detail/coronavirus-excess-deaths-tracker" },
      { name: "Our World in Data", url: "https://ourworldindata.org/excess-mortality-covid" }
    ],
    category: "infectious",
    severity: "high"
  },

  // ========== REMEDIOS CASEROS PELIGROSOS ==========
  {
    id: "REM-001",
    patterns: [
      /peróxido\s+de\s+hidrógeno\s+intravenoso/i,
      /oxígeno\s+idual\s+intravenoso/i,
      /mms\s+(clorito|cloro\s+dióxido)/i,
      /miracle\s+mineral\s+solution/i
    ],
    verdict: "false",
    confidence: 0.99,
    explanation: "El MMS (clorito de sodio) es UN PELIGRO para la salud. La FDA ha emitido múltiples advertencias. Puede causar daño renal severo, insuficiencia respiratoria y muerte.",
    sources: [
      { name: "FDA Warning", url: "https://www.fda.gov/consumers/consumer-updates/danger-dont-drink-miracle-mineral-solution-or-similar-products" },
      { name: "Poison Control", url: "https://www.poison.org/articles/miracle-mineral-solution-or-mms" }
    ],
    category: "dangerous",
    severity: "critical"
  },
  {
    id: "REM-002",
    patterns: [
      /aceite\s+de\s+orégano\s+cure\s+cancer/i,
      /aceite\s+orégano\s+cura\s+todo/i,
      /orégano\s+antibiótico\s+natural/i
    ],
    verdict: "misleading",
    confidence: 0.82,
    explanation: "El aceite de orégano tiene propiedades antioxidantes, pero NO cura el cáncer ni reemplaza antibióticos. Usarlo en lugar de tratamiento médico puede ser peligroso.",
    sources: [
      { name: "Memorial Sloan Kettering", url: "https://www.mskcc.org/cancer-care/integrative-medicine/herbs/oregano" },
      { name: "PubMed Meta-analysis", url: "https://pubmed.ncbi.nlm.nih.gov/?term=oregano+oil+antimicrobial" }
    ],
    category: "remedies",
    severity: "medium"
  },
  {
    id: "REM-003",
    patterns: [
      /coloidal\s+plata\s+cura/i,
      /plata\s+coloidal\s+inmune/i,
      /plata\s+coloidal\s+antibiótico/i
    ],
    verdict: "false",
    confidence: 0.95,
    explanation: "La plata coloidal NO tiene beneficios medicinales comprobados. Puede causar argiria (coloración permanente de la piel), daño renal y puede interferir con medicamentos.",
    sources: [
      { name: "NIH", url: "https://www.nccih.nih.gov/health/silver-colloidal" },
      { name: "FDA", url: "https://www.fda.gov/consumers/consumer-updates/silver-dont-take- orally" }
    ],
    category: "dangerous",
    severity: "high"
  },

  // ========== MENTAL HEALTH ==========
  {
    id: "MH-001",
    patterns: [
      /depresión\s+es\s+falta\s+de\s+fe/i,
      /depresión\s+no\s+existe/i,
      /tristeza\s+no\s+es\s+depresión/i,
      /ansiedad\s+es\s+debilidad/i
    ],
    verdict: "false",
    confidence: 0.95,
    explanation: "La depresión es un trastorno neurológico con base biológica. No es 'falta de fe' ni 'debilidad'. Afecta a más de 280 millones de personas en el mundo (OMS).",
    sources: [
      { name: "OMS - Depression", url: "https://www.who.int/news-room/fact-sheets/detail/depression" },
      { name: "NIMH", url: "https://www.nimh.nih.gov/health/topics/depression" }
    ],
    category: "mental-health",
    severity: "high"
  },
  {
    id: "MH-002",
    patterns: [
      /medicamentos\s+psiquiátricos\s+son\s+veneno/i,
      /antidepresivos\s+destruyen\s+cerebro/i,
      /no\s+tomes\s+antidepresivos/i
    ],
    verdict: "false",
    confidence: 0.90,
    explanation: "Los antidepresivos son tratamientos validados por décadas de investigación. Suspenderlos abruptamente puede causar síndrome de abstinencia y empeoramiento peligroso.",
    sources: [
      { name: "APA Guidelines", url: "https://www.psychiatry.org/patients-families/depression/what-is-depression" },
      { name: "NICE Guidelines", url: "https://www.nice.org.uk/guidance/cg90" }
    ],
    category: "mental-health",
    severity: "high"
  },

  // ========== ALIMENTACIÓN ==========
  {
    id: "ALI-001",
    patterns: [
      /detox\s+real\s+limpieza/i,
      /desintoxicación\s+natural/i,
      /limpiar\s+hígado\s+con/i,
      /cleanse\s+el\s+organismo/i
    ],
    verdict: "misleading",
    confidence: 0.85,
    explanation: "Tu hígado y riñones ya desintoxican tu cuerpo. Los 'detox' comerciales no tienen evidencia científica. La食品安全ade no reemplaza funciones orgánicas.",
    sources: [
      { name: "Science Based Medicine", url: "https://sciencebasedmedicine.org/a-physicians-thoughts-on-detox/" },
      { name: "NHS", url: "https://www.nhs.uk/live-well/eat-well/do-you-need-a-detox/" }
    ],
    category: "nutrition",
    severity: "medium"
  },
  {
    id: "ALI-002",
    patterns: [
      /gluten\s+causa\s+autismo/i,
      /dieta\s+sin\s+gluten\s+cura\s+autismo/i,
      /gluten\s+libre\s+y\s+autismo/i
    ],
    verdict: "false",
    confidence: 0.92,
    explanation: "No hay evidencia de que el gluten cause autismo. La dieta sin gluten es necesaria SOLO para personas con enfermedad celíaca diagnosticada profesionalmente.",
    sources: [
      { name: "Autism Speaks Research", url: "https://www.autismspeaks.org/science-and-research/our-research/research-initiatives/gluten-free-casein-free-diet" },
      { name: "Cochrane Review", url: "https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD010942.pub2/full" }
    ],
    category: "nutrition",
    severity: "medium"
  },

  // ========== ANTIBIÓTICOS ==========
  {
    id: "ANT-001",
    patterns: [
      /antibióticos\s+para\s+gripe/i,
      /antibióticos\s+viral/i,
      /tomar\s+antibióticos\s+prevención/i
    ],
    verdict: "false",
    confidence: 0.98,
    explanation: "Los antibióticos NO funcionan contra virus. Solo matan bacterias. Usarlos innecesariamente crea resistencia antibiótica, una de las mayores amenazas de salud global.",
    sources: [
      { name: "WHO - AMR", url: "https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance" },
      { name: "CDC - Antibiotic Resistance", url: "https://www.cdc.gov/antibiotic-use/community/index.html" }
    ],
    category: "antibiotics",
    severity: "high"
  },

  // ========== EMERGENCIAS ==========
  {
    id: "EME-001",
    patterns: [
      /no\s+llames?\s+a\s+ambulancia/i,
      /no\s+vayas?\s+al\s+hospital/i,
      /tratar\s+en\s+casa\s+infarto/i,
      /infarto\s+se\s+cura\s+en\s+casa/i
    ],
    verdict: "false",
    confidence: 0.99,
    explanation: "Las emergencias médicas (infarto, ACV, anafilaxia) requieren atención médica INMEDIATA. Cada minuto de retraso aumenta el riesgo de muerte o daño permanente.",
    sources: [
      { name: "AHA - Heart Attack", url: "https://www.heart.org/en/health-topics/heart-attack/warning-signs-of-a-heart-attack" },
      { name: "Stroke Association", url: "https://www.stroke.org/en/about-stroke/stroke-signs-and-symptoms" }
    ],
    category: "emergency",
    severity: "critical"
  },

  // ========== GÉNERO DE INFORMACIÓN ==========
  {
    id: "GEN-001",
    patterns: [
      /no\s+vayas?\s+al\s+médico/i,
      /médicos?\s+solo\s+quieren?\s+dinero/i,
      /big\s+pharma\s+nos\s+oculta/i,
      /la\s+cura\s+del\s+cancer\s+la\s+ocultan/i
    ],
    verdict: "misleading",
    confidence: 0.85,
    explanation: "La desconfianza generalizada hacia el sistema médico puede llevar a retrasar tratamientos que salvan vidas. Siempre consulta a un profesional de salud.",
    sources: [
      { name: "WHO - Infodemic", url: "https://www.who.int/publications/i/item/managed-Infodemic" },
      { name: "Nature Medicine", url: "https://www.nature.com/articles/s41591-020-1124-9" }
    ],
    category: "misinformation",
    severity: "high"
  }
];

// Medical claim detection patterns (Spanish + English)
const MEDICAL_PATTERNS = [
  // Direct claims about cures
  /(?:cura|curar|cur[ae]s?|trata|tratar|tratamiento)\s+(?:el|la|los|las)\s+\w+/gi,
  // "X is good for Y"
  /(?:\w+)\s+(?:es|son|está|están)\s+(?:buen[oa]s?|bueno|eficaz|efectiv[oa]?)\s+(?:para|por)\s+/gi,
  // "Don't take medication"
  /(?:no|nunca|jamás)\s+(?:tomes?|toma[s]?|us[ea]s?|use[s]?|consum[ae]s?)\s+(?:\w+\s+){0,3}(?:medicamento|fármaco|pastilla|droga)/gi,
  // "Doctors are hiding"
  /(?:médico[s]?|doctor[es]?|big\s+pharma|farmacéutica)\s+(?:oculta[n]?|mienten?|engañan?)/gi,
  // "Natural remedy"
  /(?:remedio[s]?\s+natural|cura\s+natural|tratamiento\s+natural)\s+(?:para|contra)\s+/gi,
  // "Vaccine dangers"
  /(?:vacuna[s]?\s+(?:causa[n]?|provoca[n]?|genera[n]?)\s+\w+)/gi,
  // "Cancer alternative"
  /(?:alternativ[ao]?\s+(?:al\s+)?(?:tratamiento|quimio|cirugía)\s+(?:del?\s+)?cancer)/gi,
];

// Export for use in other scripts
if (typeof window !== 'undefined') {
  window.MedScanKB = {
    knowledgeBase: MEDICAL_KNOWLEDGE_BASE,
    medicalPatterns: MEDICAL_PATTERNS
  };
}
