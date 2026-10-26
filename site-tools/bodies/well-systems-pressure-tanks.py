SLUG = 'well-systems-pressure-tanks'
SERVICE_NAME = 'Well Systems & Pressure Tanks'
KEYWORD = 'pressure tank'
SECONDARY_KEYWORDS = ['well water', 'water pressure', 'pressure switch', 'well system']
TITLE = 'Well Pressure Tanks in New Milford, CT | Cliff Canfield Plumbing'
DESCRIPTION = ('Well pressure tank replacement and well system plumbing in New Milford, Danbury and nearby CT towns. '
               'Fix low or uneven water pressure.')
IMAGE = None

HERO = dict(
    eyebrow='Well systems · New Milford, CT',
    h1='Well system &amp; pressure tank service in New Milford, CT',
    lead=('Pressure dropping, pump clicking on and off, or a tank that&rsquo;s seen better days? Get your well '
          'pressure tank and household well equipment repaired or replaced by a licensed master plumber.'),
    cta='Get a free pressure tank quote',
    panel=dict(title='Common well system problems', items=[
        'Low or uneven water pressure',
        'Pump turning on and off too often',
        'Waterlogged or failing pressure tank',
        'Pressure switch or gauge problems',
        'Leaks at the tank and fittings',
        'Treatment equipment for well water']),
)

SECTIONS = [
    dict(id='what-it-involves', eyebrow='The service', h2='What well pressure tank service involves',
         intro=('Your well pump pushes water into a pressure tank, and the tank holds that water under pressure so '
                'it is ready when you open a tap. When the tank or its controls fail, the whole house feels it.'),
         paras=['Pressure tank and well system work in your home typically includes:'],
         blocks=[dict(type='checklist', items=[
             'Diagnosing pressure problems from the tank to the taps',
             'Checking tank pre-charge and bladder condition',
             'Replacing failed or waterlogged pressure tanks',
             'Pressure switch and gauge replacement',
             'Tank tee, valves and fitting repairs',
             'Setting cut-in and cut-out pressure correctly',
             'Leak-checking every connection',
             'Testing pressure and flow at your fixtures'])]),
    dict(id='warning-signs', eyebrow='Common problems', h2='Signs your pressure tank or well system needs attention',
         intro='These are the symptoms that usually point to the pressure tank or the equipment around it:',
         blocks=[dict(type='cards', cols=3, items=[
             ('Rapid on-off cycling', 'If the pump clicks on and off every few seconds while water runs, the tank may be waterlogged. That wears out pumps fast.'),
             ('Pressure that surges and drops', 'Showers that go strong-weak-strong often mean the tank has lost its air charge.'),
             ('Low pressure throughout the house', 'Weak flow everywhere can come from switch settings, a clogged filter or tank problems.'),
             ('Water at the tank', 'Rust, sweating or leaks around the tank or tank tee mean it is time for repair or replacement.'),
             ('A tank that sounds full of water', 'Tapping the tank should sound hollow near the top. A solid sound everywhere suggests a failed bladder.'),
             ('No water at all', 'Could be the switch, wiring or the pump itself. We will track down the cause.')])],
         callout=('<strong>Pump in the well?</strong> If the problem turns out to be the pump down in the well itself, '
                  'we&rsquo;ll tell you so you can bring in the right well specialist. The pressure tank and the '
                  'equipment in your home are what we service.')),
    dict(id='options', eyebrow='Repair options', h2='Pressure tank repair and replacement options',
         intro='Depending on what we find, the fix is usually one of these:',
         blocks=[dict(type='options', items=[
             ('Quick fix', 'Pressure tank recharge', 'If the tank&rsquo;s bladder is still good, restoring the correct air pre-charge can solve cycling and pressure swings.', ['Fast, low-cost fix', 'Restores steady pressure', 'Protects your pump']),
             ('Most common', 'Pressure tank replacement', 'A new bladder-style pressure tank sized to your pump and household when the old one has failed.', ['Longer pump run times', 'Fewer pump starts', 'Sized to your home']),
             ('Controls', 'Pressure switch &amp; gauge', 'New switch, gauge and tank-tee components when controls are worn, pitted or giving false readings.', ['Accurate pressure readings', 'Correct cut-in / cut-out', 'Reliable pump control']),
             ('Water quality', 'Well water treatment', 'Sediment filters, softeners and treatment equipment to protect your system and fixtures.', ['Matched to water tests', 'Bypass for easy service', 'Protects tanks and fixtures'])])]),
    dict(id='considerations', eyebrow='Project considerations', h2='What to consider for your well system',
         intro='A few details make the difference between a quick fix and a lasting one.',
         blocks=[dict(type='consider', items=[
             ('Tank size', 'A larger tank means fewer pump starts, which helps your pump last longer. The right size depends on your pump and household.'),
             ('Pump protection', 'Short cycling from a failed tank is one of the main reasons well pumps wear out early. Fixing the tank protects the pump.'),
             ('Pressure settings', 'Switch settings and tank pre-charge have to match. Many pressure complaints come down to settings being out of sync.'),
             ('Water quality', 'Sediment, iron and hard water clog filters and wear out tanks and fixtures. Treatment may be part of the solution.'),
             ('Location &amp; access', 'Tanks in tight basements or crawl spaces can affect the work. We plan for access during the visit.'),
             ('Power &amp; safety', 'Well equipment involves both water and electricity. Repairs should be done with power safely shut off.')])]),
    dict(id='process', eyebrow='How it works', h2='Our pressure tank service process',
         intro='You will know what is wrong, what it costs and when it will be fixed.',
         blocks=[dict(type='steps', items=[
             ('Request a visit', 'Call us or send the form below and describe what your water pressure is doing.'),
             ('Diagnosis', 'We check the tank, pre-charge, switch, gauge and fittings to find the real cause.'),
             ('Clear, written quote', 'You get a written quote for the repair or replacement before work starts.'),
             ('Repair or replace', 'We replace or repair the components, set the pressures and check every connection.'),
             ('Test &amp; walkthrough', 'We test pressure at your fixtures and show you what to watch for.')])]),
    dict(id='why-us', eyebrow='Why Cliff Canfield Plumbing', h2='Why well owners choose us for pressure tank service',
         blocks=[dict(type='why')]),
]

AREA_HEADING = 'Pressure tank service in New Milford &amp; nearby towns'
AREA_TEXT = ('Based in New Milford, we service well pressure tanks and in-home well equipment for homeowners across '
             'Western Connecticut, from Brookfield, Danbury and Newtown to Ridgefield, Southbury and Roxbury. '
             'Private wells are common here, and losing water pressure is not something that can wait.')

ESTIMATE = dict(
    heading='Get your pressure tank quote',
    lead=('Tell us what your water pressure is doing and anything you&rsquo;ve noticed at the tank. We&rsquo;ll find '
          'the cause and give you a clear price.'),
    options=[('Pressure Tank', 'Pressure tank repair / replacement'), ('Low Water Pressure', 'Low or uneven water pressure'),
             ('Pressure Switch / Gauge', 'Pressure switch or gauge'), ('Well Water Treatment', 'Well water treatment'),
             ('Other', 'Something else')],
    details_label='Tell us about your well system',
    placeholder='e.g. &quot;Pump clicks on and off every few seconds when the shower runs. Tank is about 15 years old.&quot;',
)
REVIEW = dict(quote=('Cliff was on time and very knowledgeable about the work that needed to be done. He explained '
                     'everything ahead of time and was focused on fixing the issues and making sure I was happy. '
                     'I will definitely use Cliff again.'),
              name='Lee B.', initials='LB', place='Homeowner · Angi review')

FAQ_EYEBROW = 'Well system FAQ'
FAQ_HEADING = 'Pressure tank questions, answered.'
FAQS = [
    ('How much does a pressure tank replacement cost?',
     'It depends on the tank size, the condition of the switch, gauge and fittings, and how easy the tank is to reach. '
     'Sometimes a recharge or a new switch solves the problem for much less. We give you a written quote after '
     'diagnosing the system, so you know the full price before work starts.'),
    ('How do I know if my pressure tank is bad?',
     'The most common signs are the pump turning on and off rapidly while water runs, pressure that surges and drops, '
     'and a tank that sounds full of water when tapped near the top. Leaks or rust at the tank are another sign.'),
    ('How long does a pressure tank last?',
     'Many bladder-style tanks last a decade or more, but water quality, sizing and pressure settings all affect '
     'lifespan. A tank that is short-cycling should be addressed quickly to protect the pump.'),
    ('Do you replace well pumps?',
     'We service the pressure tank and the well equipment inside your home. If the problem is the pump down in the '
     'well, we will tell you so you can bring in the right well specialist.'),
    ('How quickly can you come out if I have no water?',
     'Call us at <a href="tel:+18602481218">1 (860) 248-1218</a>. We typically respond within 2&ndash;3 hours across '
     'New Milford and the surrounding towns. Check your breaker for the well pump first, and leave the pump switched '
     'off if you see water leaking at the tank.'),
]

RELATED_HEADING = 'Other services for well-water homes.'
RELATED = [
    ('water-filtration-treatment', 'Sediment filters, softeners and iron treatment matched to your well water test.'),
    ('plumbing-repairs', 'Leaks, valves, fixtures and pressure problems throughout your home, diagnosed and fixed.'),
    ('water-heater-installation', 'Water heaters replaced and installed, and protected from well water sediment.'),
]

CTA = dict(h2='Water pressure acting up?',
           p='Get a free on-site visit and a clear, written quote for your pressure tank or well equipment. No obligation.')
