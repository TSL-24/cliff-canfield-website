SLUG = 'plumbing-repairs'
SERVICE_NAME = 'Plumbing Repairs'
KEYWORD = 'plumbing repair'
SECONDARY_KEYWORDS = ['plumber', 'leak', 'water pressure', 'shut-off valve']
TITLE = 'Plumbing Repair in New Milford, CT | Cliff Canfield Plumbing'
DESCRIPTION = ('Fast plumbing repair in New Milford, Danbury and nearby CT towns. Leaks, fixtures, valves and '
               'pressure problems fixed by a licensed master plumber.')
IMAGE = None

HERO = dict(
    eyebrow='Plumbing repairs · New Milford, CT',
    h1='Plumbing repair in New Milford, CT',
    lead=('Something leaking, dripping, running or just not working right? Get a licensed master plumber who shows '
          'up on time, finds the real cause and fixes it, with a clear price before the work starts.'),
    cta='Request a plumbing repair',
    panel=dict(title='Repairs we handle every week', items=[
        'Leaking pipes, fittings and valves',
        'Dripping or broken faucets',
        'Running or leaking toilets',
        'Low water pressure',
        'Failed shut-off valves',
        'Outdoor spigots and noisy pipes']),
)

SECTIONS = [
    dict(id='what-it-involves', eyebrow='The service', h2='What our plumbing repair service covers',
         intro=('Most plumbing problems start small: a drip, a slow leak, a valve that won&rsquo;t close. Fixing them '
                'early is almost always cheaper than waiting for water damage.'),
         paras=['Every plumbing repair visit follows the same approach:'],
         blocks=[dict(type='checklist', items=[
             'Listening to what you have noticed and when',
             'Finding the actual source, not just the symptom',
             'Explaining the problem and your options',
             'A clear price before any work begins',
             'Quality parts that match your system',
             'Repairs done neatly with minimal disruption',
             'Testing the repair and checking for leaks',
             'Cleaning up before we leave'])]),
    dict(id='warning-signs', eyebrow='Common problems', h2='Common plumbing problems we repair',
         intro='These are the repairs homeowners call us for most often:',
         blocks=[dict(type='cards', cols=3, items=[
             ('Leaks and drips', 'Leaking pipes, fittings, supply lines and valves, including leaks in hidden spots that can cause damage.'),
             ('Faucet problems', 'Drips, low flow, loose handles and leaks under the sink. Some faucets need a repair, others a replacement.'),
             ('Running toilets', 'A toilet that runs or refills on its own can waste a lot of water. Usually a quick fix.'),
             ('Low water pressure', 'Weak pressure at one fixture or the whole house, from clogged aerators to failing valves or piping.'),
             ('Stuck or leaking valves', 'Old shut-off valves that won&rsquo;t turn or that leak when they do. Important to fix before an emergency.'),
             ('Noisy pipes', 'Banging, hammering or whistling pipes are often fixable and can signal pressure problems.')])],
         callout=('<strong>Water where it shouldn&rsquo;t be?</strong> Find your main shut-off valve and turn it '
                  'off, then call us. Stopping the water first limits damage while we&rsquo;re on the way.')),
    dict(id='options', eyebrow='Repair or replace', h2='Plumbing repair options',
         intro='Not every problem needs a replacement. We&rsquo;ll walk you through the options honestly:',
         blocks=[dict(type='options', items=[
             ('Most common', 'Targeted repair', 'Fix the specific part that failed, such as a cartridge, washer, fitting or valve.', ['Lowest cost', 'Quick turnaround', 'Keeps what still works']),
             ('Longer lasting', 'Component replacement', 'Replace a worn faucet, valve or section of pipe when repairs would just buy time.', ['New warranty on parts', 'Fewer future calls', 'Better performance']),
             ('Prevention', 'Shut-off &amp; valve upgrades', 'Replace old, stuck shut-off valves so you can actually turn the water off when it matters.', ['Quick to install', 'Peace of mind', 'Easier future repairs']),
             ('Bigger picture', 'System updates', 'When problems keep coming back, updating sections of old piping can be the most cost-effective fix.', ['Fewer leaks', 'Better pressure', 'Planned, not emergency'])])]),
    dict(id='considerations', eyebrow='Before we arrive', h2='What helps us fix your plumbing faster',
         intro='A few details help us diagnose the problem and bring the right parts.',
         blocks=[dict(type='consider', items=[
             ('When it started', 'Tell us when you first noticed the problem and whether it is constant or only happens sometimes.'),
             ('Where it is', 'Note which fixture, room or area is affected, and whether more than one spot has the problem.'),
             ('Photos', 'A quick photo of the leak, fixture or model label can help us plan the repair.'),
             ('Your water source', 'Let us know if you are on a private well or city water. It affects pressure and fixtures.'),
             ('Shut-off location', 'Know where your main shut-off is. We can label it for you if you&rsquo;re not sure.'),
             ('Access', 'Clearing space under sinks or around the problem area helps us get started right away.')])]),
    dict(id='process', eyebrow='How it works', h2='Our plumbing repair process',
         intro='Straightforward from the first call to the finished repair.',
         blocks=[dict(type='steps', items=[
             ('Call or send the form', 'Tell us what is going on. We typically respond within 2&ndash;3 hours.'),
             ('Diagnose', 'We find the source of the problem and explain what is wrong.'),
             ('Clear price', 'You get a clear price for the repair before any work starts.'),
             ('Repair', 'We make the repair with quality parts and test everything when we&rsquo;re done.')])]),
    dict(id='why-us', eyebrow='Why Cliff Canfield Plumbing', h2='Why homeowners call us for plumbing repair',
         blocks=[dict(type='why')]),
]

AREA_HEADING = 'Plumbing repair in New Milford &amp; nearby towns'
AREA_TEXT = ('Based in New Milford, we handle plumbing repair for homeowners across Western Connecticut, from '
             'Brookfield, Danbury and Newtown to Ridgefield, Southbury and Westport. Being local means faster response '
             'when something is leaking, and a plumber who knows the homes in your area.')

ESTIMATE = dict(
    heading='Request a plumbing repair',
    lead=('Tell us what&rsquo;s happening and where. We&rsquo;ll call you back to schedule a visit and give you a clear '
          'price before any work starts.'),
    options=[('Plumbing Repair', 'General plumbing repair'), ('Leak', 'Leak'), ('Faucet / Fixture', 'Faucet or fixture'),
             ('Toilet', 'Toilet'), ('Water Pressure', 'Water pressure'), ('Other', 'Something else')],
    details_label='Tell us what&rsquo;s going on',
    placeholder='e.g. &quot;Kitchen faucet drips constantly and the shut-off under the sink won&rsquo;t turn.&quot;',
)
REVIEW = dict(quote='Cliff was great. He was reasonably priced, came quickly and fixed the problem. I would definitely recommend his services.',
              name='Gaby L.', initials='GL', place='Homeowner · Angi review')

FAQ_EYEBROW = 'Plumbing repair FAQ'
FAQ_HEADING = 'Plumbing repair questions, answered.'
FAQS = [
    ('How much does a plumbing repair cost?',
     'It depends on the problem, the parts needed and how easy it is to reach. A faucet cartridge or toilet repair '
     'costs far less than replacing a section of pipe behind a wall. We explain the problem and give you a clear price '
     'before any work starts.'),
    ('How quickly can you come out?',
     'We typically respond within 2&ndash;3 hours across New Milford and the surrounding towns. For the fastest '
     'response, call us at <a href="tel:+18602481218">1 (860) 248-1218</a>.'),
    ('Should I repair or replace a leaking faucet or valve?',
     'Many faucets and valves can be repaired with a new cartridge or washer. If the fixture is old, corroded or '
     'parts are hard to find, replacement is often the better value. We will give you both options.'),
    ('Can you install parts or fixtures I already bought?',
     'Yes. If you have already purchased a faucet or other fixture, we can install it. Let us know the model so we can '
     'confirm it fits your plumbing.'),
    ('What should I do while I wait for a plumber?',
     'If water is leaking, turn off the closest shut-off valve or the main water shut-off, and move belongings away '
     'from the area. Turn off power to any electrical equipment near the water if it is safe to do so.'),
]

RELATED_HEADING = 'Other services homeowners often need.'
RELATED = [
    ('leak-frozen-pipe-repair', 'Active leaks, frozen pipes and burst pipes found and repaired, often without opening walls.'),
    ('fixture-installation-repair', 'Faucets, sinks, showers and tub fixtures installed or repaired, including fixtures you supply.'),
    ('toilet-repair-replacement', 'Running, leaking and wobbly toilets repaired, or replaced with a new, efficient model.'),
]

CTA = dict(h2='Something leaking or not working right?',
           p='Call now or send the form, and get a clear price for your plumbing repair before any work starts.',
           button='Request a repair')
