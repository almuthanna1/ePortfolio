import ProjectCard from "@/components/ProjectCard";  // Import the Card component

const projects = [
  { title: 'FilesMagic', desc: 'File converter web app (SEO optimized)' },
  { title: 'Nexren', desc: 'SaaS agency for startup MVPs' },
  { title: 'Fresh Pantry', desc: 'iOS app to track grocery freshness' },
];

export default function Projects() {
  return (
    <section className="py-8">
      <h2 className="text-2xl font-semibold mb-4">Projects</h2>
      <div className="grid gap-4 md:grid-cols-3">
        {projects.map((proj, i) => (
          <ProjectCard key={i} title={proj.title} desc={proj.desc} />
        ))}
      </div>
    </section>
  );
}
